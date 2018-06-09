from django.db import models

from .consts import ThemeChoices
from .fulltext import SearchManager


class User(models.Model):
    """Blogger, author, writer"""

    name = models.CharField(max_length=64, unique=True)
    alias = models.CharField(max_length=64, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # note: do not want another ``Theme`` table
    theme_scheme = models.CharField(
        max_length=64,
        default='Pisces',
        choices=ThemeChoices,
    )

    site_title = models.CharField(max_length=128, blank=True)
    site_subtitle = models.CharField(max_length=128, blank=True)
    site_desc = models.CharField(max_length=128, blank=True)

    douban_id = models.CharField(max_length=64, blank=True)
    zhihu_id = models.CharField(max_length=64, blank=True)
    weibo_id = models.CharField(max_length=64, blank=True)
    twitter_id = models.CharField(max_length=64, blank=True)
    facebook_id = models.CharField(max_length=64, blank=True)
    github_id = models.CharField(max_length=64, blank=True)
    instagram_id = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

    objects = SearchManager(['title', 'body'])

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True)

    # many-to-many field, use blank=True instead of null=True
    tags = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=200)
    body = models.TextField()

    is_top = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # if not published, treat as post draft.
    publish_at = models.DateTimeField(blank=True, null=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def gather_posts_categories(cls, posts):
        """
        :param posts: Post objects list.
        :rtype: Category objects list.
        """
        categories = set()
        for post in posts:
            categories.add(post.category)
        return list(categories)

    @classmethod
    def gather_posts_tags(cls, posts):
        tags = set()
        for post in posts:
            for tag in post.tags.all():
                tags.add(tag)
        return list(tags)

    @classmethod
    def to_dict(cls, post):
        return {
            'id': post.pk,
            'is_top': post.is_top,
            'category': '' if post.category is None else post.category.name,
            'author': post.author.name,
            'title': post.title,
            'body': post.body,
            'tags': [tag.name for tag in post.tags.all()],
        }
