from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    # lists
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
)


app_name = "user"
urlpatterns = [
    # user:registration
    path("registration", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path(
        # breaking lines
        "reset-password",
        views.password_reset,
        name="reset-password",
    ),
    path(
        #
        "password-reset-done",
        PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        #
        "password-reset-confirm/<uidb64>/<token>",
        views.password_reset_confirm_view,
        name="password_reset_confirm",
    ),
    path(
        #
        "password-reset-complete",
        views.password_reset_complete_view,
        name="password_reset_complete",
    ),
]
