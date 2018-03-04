from urllib.parse import urlunparse

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from feedgen.feed import FeedGenerator

from .models import Post, Category
from .forms import NewPostForm
from .utils import mdtohtml


def check_health(request):
    return HttpResponse('semo ok.')


def feed_atom(request):
    author = request.blogger
    host = request.get_host()
    path = reverse('blog:posts')
    blogs_url = urlunparse(('http', host, path, '', '', ''))
    posts = Post.objects.filter(author=author)
    last_updated = sorted(posts, key=lambda post: post.update_at)[-1].update_at
    fg = FeedGenerator()
    fg.id(blogs_url)
    fg.title("{author}'s blog ".format(author=author))
    fg.author({'name': author.name})
    fg.link(href=urlunparse(('http', host, '', '', '', '')))
    fg.subtitle('try to be awesome???')
    fg.updated(updated=last_updated)

    for post in posts:
        fe = fg.add_entry()
        path = reverse('blog:post', kwargs={'post_id': post.id})
        url = urlunparse(('http', host, path, '', '', ''))
        fe.id(path)
        fe.title(post.title)
        fe.link(href=url)
        fe.updated(updated=post.update_at)
        fe.content(mdtohtml(post.body))

    return HttpResponse(fg.atom_str(),
                        content_type="application/xml")


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
    md = mdtohtml(post.body)
    return render(request, 'blog/edit.html', {
        'content': md,
        'author': author,
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
        author = request.blogger
        post = Post.objects.get(id=post_id)
        md = mdtohtml(post.body)

        return render(request, 'blog/post.html', {
            'content': md,
            'post': post,
            'author': author,
        })
