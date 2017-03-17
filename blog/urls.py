from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^check_health$', views.check_health, name='check_health'),
    url(r'^$', views.Blogs.as_view(), name='index'),
    url(r'^tags$', views.Blogs.as_view(), name='show_tags'),
    url(r'^blogs$', views.Blogs.as_view(), name='posts'),
    url(r'^blogs/search$', views.search, name='search'),
    url(r'^blogs/new$', views.new_blog, name='new_post'),
    url(r'^blogs/(?P<post_id>\d+)$', views.Blog.as_view(), name='post'),
    url(r'^blogs/(?P<post_id>\d+)/edit$', views.edit_blog, name='edit_post'),
]
