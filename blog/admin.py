from django.contrib import admin
from .models import User, Category, Post, Tag, Host

admin.site.register(User)
admin.site.register(Host)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
