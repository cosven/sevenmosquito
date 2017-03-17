from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.template import loader

from .models import Post, User, Category
from .forms import NewPostForm, EditPostForm
from .utils import mdtohtml


def check_health(request):
    return HttpResponse('semo ok.')


@login_required(login_url='admin:login')
def new_blog(request):
    author = request.blogger
    posts = Post.objects.filter(author=author)
    categories = Category.objects.all()
    tags = Post.gather_posts_tags(posts)
    return render(request, 'blog/new.html', {
        'categories': categories,
        'tags': tags
    })


@login_required(login_url='admin:login')
def edit_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    author = request.blogger
    posts = Post.objects.filter(author=author)
    categories = Category.objects.all()
    tags = Post.gather_posts_tags(posts)
    return render(request, 'blog/edit.html', {
        'post': post,
        'categories': categories,
        'tags': tags
    })


class Blogs(View):

    def get(self, request):
        author = request.blogger
        posts = Post.objects.filter(author=author).order_by('-create_at')

        return render(request, 'blog/index.html', {'posts': posts})

    @method_decorator(login_required)
    def post(self, request):
        """create blog"""
        # TODO: set login_url for login_required
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.apply(request.blogger)
            return JsonResponse({'message': 'ok'})
        else:
            return JsonResponse({'message': 'validate failed'})


class Blog(View):

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        md = mdtohtml(post.body)

        return render(request, 'blog/post.html', {
            'content': md,
            'post': post,
        })

    @method_decorator(login_required)
    def post(self, request, post_id):
        form = EditPostForm(request.POST)
        if form.is_valid():
            form.apply(request.blogger, post_id)
            return redirect('blog:post', post_id=post_id)
        else:
            return JsonResponse('blog:edit_post', post_id=post_id)


def search(request):
    posts = Post.objects.filter(author=request.blogger).order_by('-create_at')
    return JsonResponse([Post.to_dict(post) for post in posts], safe=False)
