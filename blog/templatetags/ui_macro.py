from django import template

register = template.Library()


@register.inclusion_tag('blog/_macro/blogger_overview.html')
def show_blogger_overview(request, posts, categories, tags):
    return {
        'request': request,
        'posts': posts,
        'categories': categories,
        'tags': tags
    }
