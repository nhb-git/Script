from django.urls import path, re_path
from blogs import views

urlpatterns = [
    path("login/", views.login, name="login"),
]
