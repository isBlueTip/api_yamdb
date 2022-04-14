from titles.models import Categories
from titles.serializers import CategoriesSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
