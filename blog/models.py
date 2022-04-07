from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Post(models.Model):
    STATUS_CHOISES = (
        ("draft",      "Draft"),
        ("published",  "Published")
    )

    title               = models.CharField(max_length=200)
    slug                = models.SlugField(max_length=250, unique_for_date="publish")
    author              = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body                = models.TextField()
    publish             = models.DateTimeField(default=timezone.now)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    status              = models.CharField(max_length=10, default="draft", choices=STATUS_CHOISES)
    tags                = TaggableManager()

    class Meta:
        ordering = ("-publish", )
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post                = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name                = models.CharField(max_length=80)
    body                = models.TextField()
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    active              = models.BooleanField(default=True)

    class Meta:
        ordering = ("created", )
    
    def __str__(self):
        return f"comment by '{self.name}' on '{self.post}'"