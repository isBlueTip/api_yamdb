from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from api.filters import TitleFilter
from api.permissions import IsAdminOrReadOnly
from api.titles_mixins import CreateListDestroyViewSet
from api.titles_serializers import (CategorySerializer, GenreSerializer,
                                    TitlePostSerializer, TitleSerializer)
from titles.models import Category, Genre, Title


class CategoryViewSet(CreateListDestroyViewSet, viewsets.GenericViewSet):
    """Viewset to work with categories."""
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class GenreViewSet(CreateListDestroyViewSet, viewsets.GenericViewSet):
    """Viewset to work with genres."""
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    """Viewset to work with titles."""
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TitleSerializer
        return TitlePostSerializer
