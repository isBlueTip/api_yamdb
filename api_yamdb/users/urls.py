from django.urls import path
from api.users_views import SignupView, TokenView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='request_confirmation'),
    path('token/', TokenView.as_view(), name='obtain_token'),
]
