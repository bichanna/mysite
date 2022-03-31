from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

class PostListView(View):
    """
        Handles everything that's related to something list of blog posts.
    """
    def get(self, request):
        post_objects = Post.objects.filter(status="published")
        paginator = Paginator(post_objects, 10)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context = {
            "posts": posts,
            "page": page,
        }

        return render(request, "blog/post/list.html", context=context)


class PostDetailView(View):
    """
        Handles everthing that's related to post-detail views.
    """
    def get(self, request, post):
        post = get_object_or_404(Post, status="published", slug=post)
        context = {"post": post}
        return render(request, "blog/post/detail.html", context=context)
