from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homePage"),
    path("<int:blog>", views.blogByNumber),
    path("<str:blog>", views.readBlog, name="read")
]
