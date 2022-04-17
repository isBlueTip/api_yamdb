from titles.models import Category, Genre, Title
from .titles_serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    TitlePostSerializer,
)
from rest_framework import filters
from .permissions import IsAdmin
from django.shortcuts import get_object_or_404


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "category__slug",
        "genre__slug",
        "year",
    )

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        new_queryset = Title.objects.filter(title=title)
        return new_queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TitleSerializer
        return TitlePostSerializer
