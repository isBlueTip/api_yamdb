from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework import viewsets


class CreateListDestroyViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass
