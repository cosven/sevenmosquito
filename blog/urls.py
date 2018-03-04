from django.conf.urls import url

from . import views
from blog.api.v1 import Search, Blog, check_health


urlpatterns = [
    url(r'^check_health$', views.check_health, name='check_health'),
    url(r'^atom.xml$', views.feed_atom, name='feed_atom'),
    url(r'^$', views.Blogs.as_view(), name='index'),
    url(r'^tags$', views.Blogs.as_view(), name='show_tags'),
    url(r'^blogs$', views.Blogs.as_view(), name='posts'),
    url(r'^blogs/new$', views.new_blog, name='new_post'),
    url(r'^blogs/(?P<post_id>\d+)$', views.Blog.as_view(), name='post'),
    url(r'^blogs/(?P<post_id>\d+)/edit$', views.edit_blog, name='edit_post'),

    url(r'^api/v1/check_health', check_health, name='api_v1_check_health'),
    url(r'^api/v1/posts/(?P<post_id>\d+)$', Blog.as_view(), name='api_v1_blog'),
    url(r'^api/v1/posts/search', Search.as_view(), name='api_v1_search'),
]
