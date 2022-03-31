from django.contrib import admin
from .models import Post

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
    raw_id_fields = ["author"]
    ordering = ["status", "publish"]
    date_hierarchy = "publish"
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title", "body"]