from django.shortcuts import render
from blog.models import Post, Comment


def post_index(request):
    posts = Post.objects.all().order_by("-created")
    context = {
        "posts": posts,
    }

    return render(request, "post/index.html", context)


def post_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category,
    ).order_by("-created")

    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "post/category.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "post/detail.html", context)
