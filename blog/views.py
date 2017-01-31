from django.http import HttpResponse
from django.shortcuts import render


def check_health(request):
    return HttpResponse('semo ok.')


def index(request):
    return render(request, 'blog/index.html', {})


def yannnli_index(request):
    return HttpResponse("<h1>Yannnli, you're the best. oyi ~</h1>")
