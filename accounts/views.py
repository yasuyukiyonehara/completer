from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 新規作成したユーザーでログイン
            return redirect("home")  # ログイン後に移動するページ
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

def profile(request, username):
    user = get_object_or_404(User, username=username)

    post = user.post_set.all()
    return render(request, "accounts/profile.html", {"profile_user": user, "posts": posts})