from django.shortcuts import redirect, render, HttpResponse
from blog_posts.forms import BlogPostForm

from blog_posts.models import BlogPostModel
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


# def home(request):
#     blogs = BlogPostModel.objects.all().order_by("-published_at")
#     return render(request, "blog_posts/home.html", {"blogs": blogs})


def about(request):
    return HttpResponse("<h1>Listen About Us</h1>")


# def blog(request, blog_id):
#     blog = BlogPostModel.objects.get(id=blog_id)
#     return render(request, "blog_posts/blog.html", {"blog": blog})


# def update_blog(request, blog_id):
#     blog = BlogPostModel.objects.get(id=blog_id)
#     if blog.author == request.user:
#         if request.method == "POST":
#             form = BlogPostForm(data=request.POST, instance=blog)
#             if form.is_valid():
#                 form.save()
#                 return redirect("blog_posts:home")
#         form = BlogPostForm(instance=blog)
#         return render(request, "blog_posts/edit_blog.html", {"blog": blog, "form": form})
#     return HttpResponse("<h2>The page doesn't exist or you don't have permission to access</h2>")


# def delete(request, blog_id):
#     blog = BlogPostModel.objects.get(id=blog_id)
#     if request.user == blog.author:
#         blog.delete()
#         return redirect("blog_posts:home")


# def create_blog(request):
#     if request.method == "POST":
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             kwargs = {
#                 "author": request.user,
#                 "content": form.cleaned_data["content"],
#                 "published_at": form.cleaned_data["published_at"],
#                 "title": form.cleaned_data["title"],
#             }
#             BlogPostModel.objects.create(**kwargs)

#             return redirect("blog_posts:home")
#     form = BlogPostForm()
#     return render(request, "blog_posts/new_blog.html", {"form": form})


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPostModel
    fields = ("title", "content")
    template_name = "blog_posts/new_blog.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.instance)
        return super().form_valid(form)


create_blog = BlogCreateView.as_view()


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPostModel
    fields = ("title", "content")
    template_name = "blog_posts/new_blog.html"

    def is_valid(self, form):
        return super().is_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


update_blog = BlogUpdateView.as_view()


class BlogDetailView(DetailView):
    model = BlogPostModel
    context_object_name = "blog"
    template_name = "blog_posts/blog.html"
    pk_url_kwarg = "blog_id"

    # def get_context_data(self, **kwargs):
    #     kwargs.update({"user_info": self.request.user})
    #     return super().get_context_data(**kwargs)


blog = BlogDetailView.as_view()


class BlogListView(ListView):
    model = BlogPostModel
    context_object_name = "blogs"
    pk_url_kwarg = "blog_id"
    template_name = "blog_posts/home.html"
    ordering = ("-published_at",)
    paginate_by = 5


home = BlogListView.as_view()


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPostModel
    template_name = "blog_posts/confirm_delete.html"
    pk_url_kwarg = "blog_id"
    success_url = "/"

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


delete = BlogDeleteView.as_view()
