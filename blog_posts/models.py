from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# Create your models here.


class BlogPostModel(models.Model):
    title = models.CharField(_("Blog Title"), max_length=150)
    content = models.TextField(_("Content"))
    published_at = models.DateField(_("Published Date"), default=timezone.now)
    last_modified_at = models.DateField(default=timezone.now)
    author = models.ForeignKey("user.CustomUserModel", verbose_name=_("Author"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog_posts:blog", kwargs={"blog_id": self.pk})
