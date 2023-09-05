from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homePage"),
    path("posts", views.blogs, name="postsPage"),
    path("posts/<slug:slug>", views.readBlog, name="read")
]
