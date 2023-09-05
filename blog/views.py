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
    pass


def readBlog(request, blog):
    try:
        blog_title = blog
        blog_content = Allblogs[blog]
        return render(request, "blog/blog.html", {
            "selected_blog": blog_title,
            "content": blog_content
        })
    except:
        return Http404()
