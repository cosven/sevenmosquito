# -*- coding:utf8 -*-

from django import forms
from .models import User, Post, Category, Tag


class NewPostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    category = forms.IntegerField(required=False)
    tags = forms.CharField(required=False)

    def apply(self, blogger):
        author = User.objects.get(name=blogger)
        category_id = self.cleaned_data['category']
        if category_id:
            category = Category.objects.get(id=category_id)
        else:
            category = None

        post = Post.objects.create(
            title=self.cleaned_data['title'],
            author=author,
            body=self.cleaned_data['body'],
            category=category)

        if self.cleaned_data['tags']:
            for tag in self.cleaned_data['tags'].split(', '):
                tag_objects = Tag.objects.filter(name=tag)
                if tag_objects:
                    tag_object = tag_objects[0]
                else:
                    tag_object = Tag(name=tag)
                    tag_object.save()
                post.tags.add(tag_object)
