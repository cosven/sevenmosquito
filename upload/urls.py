from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Upload.as_view(), name='upload'),
]
