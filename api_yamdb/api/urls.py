from django.urls import path, include

urlpatterns = [  # добалять путь до urls своего приложения
                 # например, ('v1/auth/', include('users.urls'))
    path('v1/auth/', include('users.urls'))
]
