from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.reviews_serializers import CommentSerializer, ReviewSerializer
from titles.models import Title
from reviews.models import Review
from api.permissions import IsAuthorOrReadOnly, IsAdmin, IsModer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ('list', 'create', 'retrieve'):
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthorOrReadOnly | IsAdmin | IsModer]

        return super(CommentViewSet, self).get_permissions()

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        title_id=self.kwargs.get('title_id'))


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ('list', 'create', 'retrieve'):
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthorOrReadOnly | IsAdmin | IsModer]

        return super(CommentViewSet, self).get_permissions()

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        review_id=self.kwargs.get('review_id'))
