from django.urls import path
from news import views


urlpatterns = [
    path("login/", views.login, name="login"),
]
