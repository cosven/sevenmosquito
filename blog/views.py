import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.template import loader

from .models import Post, User
from .forms import NewPostForm
from .utils import mdtohtml


def check_health(request):
    return HttpResponse('semo ok.')


def blogs(request):
    return HttpResponse()


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


class Blogs(View):

    def get(self, request):
        author = User.objects.get(name=request.blogger)
        posts = Post.objects.filter(author=author)

        tmpl = loader.get_template('blog/index.html')
        return HttpResponse(tmpl.render({'posts': posts}, request))

    @method_decorator(login_required)
    def post(self, request):
        """create blog"""
        # TODO: set login_url for login_required
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.apply(request.blogger)
            return JsonResponse({'message': 'ok'})
        else:
            print(form.errors)
            return JsonResponse({'message': 'validate failed'})

