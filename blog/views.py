from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

Allblogs = {
    "blog1": "hey you",
    "blog2": "hi you",
    "blog3": "you you"
}


def index(request):
    blogs = list(Allblogs.keys())

    return render(request, "blog/index.html", {
        "listOfBlogs": blogs
    })


def blogs(request):
    return render(request, "blog/all-posts.html")


def readBlog(request, slug):
    return render(request, "blog/single-post.html")
