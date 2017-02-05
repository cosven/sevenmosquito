from django.http import HttpResponse
from django.shortcuts import render
import markdown2

from .models import Post


def check_health(request):
    return HttpResponse('semo ok.')


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def show_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    md = markdown2.markdown(post.body)
    return render(request, 'blog/post.html', {'content': md})


def yannnli_index(request):
    return HttpResponse("<h1>Yannnli, oyi ~</h1>")
