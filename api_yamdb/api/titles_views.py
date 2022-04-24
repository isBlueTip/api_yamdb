from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from api.titles_serializers import (CategorySerializer,
                                    GenreSerializer,
                                    TitlePostSerializer,
                                    TitleSerializer)
from titles.models import Category, Genre, Title

from .filters import TitleFilter
from .permissions import IsAdmin, IsAdminOrReadOnly, ReadOnly
from .titles_mixins import CreateListDestroyViewSet


class CategoryViewSet(
    CreateListDestroyViewSet,
    viewsets.GenericViewSet,
):
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class GenreViewSet(CreateListDestroyViewSet, viewsets.GenericViewSet):
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            self.permission_classes = [
                ReadOnly,
            ]
        elif self.action in (
            "create",
            "update",
            "partial_update",
            "destroy",
        ):
            self.permission_classes = [
                IsAdmin,
            ]

        return super(TitleViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TitleSerializer
        return TitlePostSerializer
