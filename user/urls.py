from django.urls import path

from user.views import CreateUserView

app_name = "auth"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
]
