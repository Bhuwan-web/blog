from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from .forms import UserForm
from userprofile.forms import ProfileUpdateForm
from django.views.generic import ListView
from blog_posts.models import BlogPostModel


User = get_user_model()
# Create your views here.
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    posts = user.blogpostmodel_set.all().order_by("-published_at")
    return render(request, "userprofile/profile.html", {"user_info": user, "blogs": posts})


def edit_profile(request):

    if request.method == "POST":
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile:profile", user_id=f"{request.user.id}")
    context = {
        # dict_obj
        "u_form": UserForm(instance=request.user),
        "p_form": ProfileUpdateForm(instance=request.user.profile),
    }

    return render(request, "userprofile/update_profile.html", context)


class ProfileView(ListView):
    model = BlogPostModel
    paginate_by = 3
    context_object_name = "blogs"
    template_name = "userprofile/profile.html"

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return self.model.objects.filter(author=user).order_by("-published_at")
        this_user = user

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get("user_id"))
        kwargs.update({"user_info": user})
        return super().get_context_data(**kwargs)


profile = ProfileView.as_view()
