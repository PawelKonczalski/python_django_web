from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.all()
    return render(request, 'post.html', {'post': post, 'posts': posts})


def about(request):
    return render(request, 'about.html', {})