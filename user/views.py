from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import LoginForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView

User = get_user_model()
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = UserForm()
    return render(request, "user/registration.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            data = form.cleaned_data
            if authenticate(**data):
                user = User.objects.get(username=username)
                login(request, user)
                return redirect("blog_posts:home")
            messages.warning(request, "Either Username or password is incorrect!!")

    else:
        form = LoginForm()
    return render(request, "user/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("user:login")


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "user/password_reset_email.html"
    template_name = "user/password_reset_form.html"
    success_url = reverse_lazy("user:password_reset_done")


password_reset = CustomPasswordResetView.as_view()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_view = "user/password_reset_confirm.html"
    success_url = reverse_lazy("user:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "user/password_reset_complete.html"


password_reset_complete_view = CustomPasswordResetCompleteView.as_view()
password_reset_confirm_view = CustomPasswordResetConfirmView.as_view()
