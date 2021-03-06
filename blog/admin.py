from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "publish",
        "status",
        "slug"
    ]
    list_filter = [
        "status",
        "publish",
        "created",
        "author",
    ]
    ordering = ["status", "publish"]
    date_hierarchy = "publish"
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title", "body"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "post",
        "created",
        "active",
    ]
    list_filter = [
        "created",
        "updated",
        "active",
    ]
    search_fields = ["name", "body"]