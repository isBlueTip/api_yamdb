from django.urls import path
from django.urls import path, include
from rest_framework import routers
from api.titles_views import CategoryViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()

router.register("categories", CategoryViewSet, basename="categories")
router.register("genres", GenreViewSet, basename="genres")
router.register("titles", TitleViewSet, basename="titles")

urlpatterns = [
    path("", include(router.urls)),
]
