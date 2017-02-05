from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    alias = models.CharField(max_length=64, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category, blank=True, null=True)

    # many-to-many field, use blank=True instead of null=True
    tags = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=200)
    body = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # if not published, treat as post draft.
    publish_at = models.DateTimeField(blank=True, null=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
