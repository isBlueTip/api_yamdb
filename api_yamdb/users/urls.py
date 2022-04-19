from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.users_views import SignupView, MeView, TokenView, UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='request_confirmation'),
    path('token/', TokenView.as_view(), name='obtain_token'),
    path('me/', MeView.as_view(), name='user_detail'),
    path('', include(router.urls)),
]
