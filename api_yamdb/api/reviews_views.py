from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAdmin, IsAuthorOrReadOnly, IsModer
from api.reviews_serializers import CommentSerializer, ReviewSerializer
from reviews.models import Review
from titles.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    """Viewset to work with reviews."""
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly & (IsAuthorOrReadOnly | IsAdmin | IsModer)
    ]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user,
                        title_id=title.id)


class CommentViewSet(viewsets.ModelViewSet):
    """Viewset to work with comments."""
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly & (IsAuthorOrReadOnly | IsAdmin | IsModer)
    ]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user,
                        review_id=review.id)
