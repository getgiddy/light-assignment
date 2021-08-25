from django.urls import path
from main.views import home, logout, signup, login

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path("signup", signup, name="signup"),
    path("logout", logout, name="logout"),
]
