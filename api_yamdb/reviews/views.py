from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.serializers import CommentSerializer, ReviewSerializer
from titles.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        self.title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return self.title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(title=self.title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        self.review = get_object_or_404(title.reviews.all(),
                                        pk=self.kwargs.get('review_id'))
        return self.review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(review=self.review)
