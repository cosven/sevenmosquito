from django.contrib import admin
from .models import User, Category, Post, Tag

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
