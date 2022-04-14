from django.urls import path, include

urlpatterns = [
    path(..., include(...)),  # добалять путь до urls своего приложения
                              # например, ('v1/auth/', include('users.urls'))
]
