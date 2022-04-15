from django.urls import include, path

urlpatterns = [  # добалять путь до urls своего приложения
                 # например, ('v1/auth/', include('users.urls'))
    path('v1/auth/', include('users.urls')),
    path('v1/', include('reviews.urls')),
]
