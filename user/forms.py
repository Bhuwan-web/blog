from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from user.models import LoginModel

USER = get_user_model()


class UserForm(UserCreationForm):
    super(UserCreationForm)

    class Meta:
        model = USER
        fields = ("username",)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = LoginModel
        fields = "__all__"
