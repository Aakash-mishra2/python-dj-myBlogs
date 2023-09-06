from django.shortcuts import render
from datetime import date
# Create your views here.

Allblogs = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Sky",
        "date": date(2022, 5, 13),
        "title": "Mountain Hikng",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Sky",
        "date": date(2022, 7, 21),
        "title": "Programming is fun ",
        "excerpt": "Have you ever spent hours searching that one error in one component page of your application. ",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Sky",
        "date": date(2022, 7, 21),
        "title": "Programming is fun ",
        "excerpt": "Have you ever spent hours searching that one error in one component page of your application. ",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vestibulum ultrices mi vitae hendrerit. Cras in eros quis leo .
        """
    }
]


def getDate(post):
    return post['date']


def index(request):
    sorted_posts = sorted(Allblogs, key=getDate)
    latest_posts = sorted_posts[-3:]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def blogs(request):
    return render(request, "blog/all-posts.html")


def readBlog(request, slug):
    return render(request, "blog/single-post.html")
