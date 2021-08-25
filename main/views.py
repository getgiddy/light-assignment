from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


@login_required(login_url="login")
def home(request):
    context = {"page_title": "Home"}
    return render(request, "index.html", context)


def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")

    context = {"page_title": "Signup", "form": form}
    return render(request, "signup.html", context)


def login(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")

    context = {"page_title": "Login", "form": form}
    return render(request, "login.html", context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect("login")
