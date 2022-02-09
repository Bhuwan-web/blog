from django.db import models
from user.models import CustomUserModel
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics", default="default.png")

    def __str__(self):
        return f"{self.user}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_path = self.profile_pic.path
        img = Image.open(img_path)
        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(img_path)
