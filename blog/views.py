from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Comment, Post


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
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "post/detail.html", context)
