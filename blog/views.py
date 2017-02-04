from django.http import HttpResponse
from django.shortcuts import render
import markdown2


def check_health(request):
    return HttpResponse('semo ok.')


def index(request):
    return render(request, 'blog/index.html', {})


def show_blog(request):
    with open('test.md') as f:
        md = markdown2.markdown(f.read())
        return render(request, 'blog/post.html', {'content': md})


def yannnli_index(request):
    return HttpResponse("<h1>Yannnli, oyi ~</h1>")
