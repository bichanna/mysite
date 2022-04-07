from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("tags/<slug:tag_slug>/", views.PostListView.as_view(), name="post_list_&_tag"),
    path("<slug:post>/", views.PostDetailView.as_view(), name="post_detail"),
]