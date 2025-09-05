from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post_objects.all().order_by("-created_at")
    return render(request, "post/post_list.html", {"posts": posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    return render(request, "posts/post_detail.html", {"post": post, "comments": comments})