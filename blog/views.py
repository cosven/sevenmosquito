from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, User, Category
from .utils import mdtohtml


def check_health(request):
    return HttpResponse('semo ok.')


def index(request):
    author = User.objects.get(name=request.blogger)
    posts = Post.objects.filter(author=author)
    categories = set()
    tags = set()

    for post in posts:
        categories.add(post.category)
        tags.add(post.tags.all())

    return render(request, 'blog/index.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags
    })


def show_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    md = mdtohtml(post.body)

    author = User.objects.get(name=request.blogger)
    posts = Post.objects.filter(author=author)
    categories = set()
    tags = set()

    for post in posts:
        categories.add(post.category)
        tags.add(post.tags.all())

    return render(request, 'blog/post.html', {
        'content': md,
        'post': post,
        'posts': posts,
        'categories': categories,
        'tags': tags
    })
