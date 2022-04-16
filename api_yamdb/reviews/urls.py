from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.reviews_views import CommentViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
]
