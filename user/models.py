from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserModel(AbstractUser):
    pass


class LoginModel(models.Model):
    username = models.CharField(_("Username"), max_length=50)
    password = models.CharField(_("Password"), max_length=50)
