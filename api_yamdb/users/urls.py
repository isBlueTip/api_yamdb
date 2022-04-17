from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.users_views import SignupView, TokenView, UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='request_confirmation'),
    path('token/', TokenView.as_view(), name='obtain_token'),
]
