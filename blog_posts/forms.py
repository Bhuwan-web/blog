from dataclasses import fields
from django import forms

from blog_posts.models import BlogPostModel


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ("title", "content", "published_at")
