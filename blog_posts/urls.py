from django.urls import path

from . import views

app_name = "blog_posts"

urlpatterns = [
    # localhost/
    # blog_posts:home
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("blog/<int:blog_id>", views.blog, name="blog"),
    path("blog/edit/<int:pk>", views.update_blog, name="edit"),
    path("blog/delete/<int:blog_id>", views.delete, name="delete"),
    path("blog/create", views.create_blog, name="create"),
]
