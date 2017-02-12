from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, User
from .utils import mdtohtml


def check_health(request):
    return HttpResponse('semo ok.')


def index(request):
    author = User.objects.get(name=request.blogger)
    posts = Post.objects.filter(author=author)

    return render(request, 'blog/index.html', {
        'posts': posts,
    })


def show_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    md = mdtohtml(post.body)

    return render(request, 'blog/post.html', {
        'content': md,
        'post': post,
    })


@login_required(login_url='admin:login')
def new_blog(request):
    author = User.objects.get(name=request.blogger)
    posts = Post.objects.filter(author=author)
    categories = Post.gather_posts_categories(posts)
    tags = Post.gather_posts_tags(posts)
    return render(request, 'blog/editor.html', {
        'categories': categories,
        'tags': tags
    })
