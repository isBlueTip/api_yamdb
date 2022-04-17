from django.urls import include, path

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/', include('reviews.urls')),
    path('v1/users/', include('users.urls')),
]
