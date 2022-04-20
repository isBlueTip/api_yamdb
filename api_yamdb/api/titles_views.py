from titles.models import Category, Genre, Title
from api.titles_serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    TitlePostSerializer,
)
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
)
from rest_framework import filters
from rest_framework import viewsets
from .permissions import IsAdmin, ReadOnly, AdminOrReadOnly
from rest_framework.decorators import action


@action(detail=True, gmethods=["get", "post", "delete"])
class CategoryViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [
        AdminOrReadOnly,
    ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


@action(detail=True, gmethods=["get", "post", "delete"])
class GenreViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [
        AdminOrReadOnly,
    ]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    lookup_field = "slug"


class TitleFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__slug")
    genre = django_filters.CharFilter(field_name="genre__slug")
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )
    year = django_filters.NumberFilter(field_name="year")

    class Meta:
        model = Title
        fields = {"category", "genre", "name", "year"}


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
