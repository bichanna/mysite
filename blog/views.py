from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Post
from .forms import CommentForm

from taggit.models import Tag

class PostListView(View):
    """
        Handles everything that's related to something list of blog posts.
    """
    def get(self, request, tag_slug=None):
        post_objects = Post.objects.filter(status="published")

        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            post_objects = post_objects.filter(tags__in=[tag])

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
            "tag": tag,
        }

        return render(request, "blog/post/list.html", context=context)


class PostDetailView(View):
    """
        Handles everthing that's related to post-detail views.
    """
    def get(self, request, post):
        post = get_object_or_404(Post, status="published", slug=post)
        comments = post.comments.filter(active=True)
        comment_form = CommentForm()

        # get similar posts
        tag_ids = post.tags.values_list("id", flat=True)
        similar_posts = Post.objects.filter(
            status="published",
            tags__in=tag_ids,
        ).exclude(id=post.id).annotate(same_tags_num=Count("tags")).order_by("-same_tags_num", "-publish")[0:4]
        
        context = {
            "post": post,
            "comments": comments,
            "new_comment": False,
            "comment_form": comment_form,
            "similar_posts": similar_posts,
        }
        return render(request, "blog/post/detail.html", context=context)
    
    def post(self, request, post):
        post = get_object_or_404(Post, status="published", slug=post)
        comments = post.comments.filter(active=True)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            pass
        
        context = {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        }
        return render(request, "blog/post/detail.html", context=context)