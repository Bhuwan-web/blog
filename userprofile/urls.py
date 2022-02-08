from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    # profile:<username>
    path("<int:user_id>", views.profile, name="profile"),
    path("edit/", views.edit_profile, name="edit"),
]
