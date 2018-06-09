from django import template
from blog.models import Post, User

register = template.Library()


@register.inclusion_tag('blog/_macro/blogger_overview.html')
def show_blogger_overview(request):
    author = User.objects.get(name=request.blogger)
    posts = Post.objects.filter(author=author)
    categories = Post.gather_posts_categories(posts)
    tags = Post.gather_posts_tags(posts)

    return {
        'request': request,
        'posts': posts,
        'categories': categories,
        'tags': tags
    }


@register.inclusion_tag('blog/_macro/post_title_overview.html')
def show_post_title_overview(post):
    return {'post': post}
