from django.contrib import admin
from .models import BlogPostModel

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "author", "published_at")
    fields = ("title", "author", "published_at")
    list_filter = ("author",)


admin.site.register(BlogPostModel, PostAdmin)
