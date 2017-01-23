from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64, blank=True)
    avatar = models.URLField(blank=True)
    email = models.EmailField(blank=True)


class Post(models.Model):
    author = models.ForeignKey(User)

    title = models.CharField(max_length=200)
    body = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True)
    delete_at = models.DateTimeField(auto_now_add=True, blank=True)


class Tag(models.Model):
    pass
