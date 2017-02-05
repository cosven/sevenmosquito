from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^check_health$', views.check_health, name='check_health'),
    url(r'^$', views.index, name='index'),
    url(r'^blogs/(?P<post_id>\d+)/$', views.show_blog, name='show_blog'),
]
