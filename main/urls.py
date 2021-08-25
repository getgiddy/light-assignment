from django.urls import path
from main.views import home, signup, login

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path("signup", signup, name="signup"),
]
