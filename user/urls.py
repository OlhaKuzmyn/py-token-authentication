from django.urls import path

from user.views import CreateUserView, CreateTokenView

app_name = "auth"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", CreateTokenView.as_view(), name="login"),
]
