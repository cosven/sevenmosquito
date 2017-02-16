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


class EditPostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    category = forms.IntegerField(required=False)
    tags = forms.CharField(required=False)

    def apply(self, blogger, post_id):
        post = Post.objects.get(id=post_id)

        category_id = self.cleaned_data['category']
        if category_id:
            category = Category.objects.get(id=category_id)
        else:
            category = None

        Post.objects.filter(id=post_id).update(
            title=self.cleaned_data['title'],
            body=self.cleaned_data['body'],
            category=category
        )

        old_tags = post.tags.all()
        tags_str = self.cleaned_data['tags'].strip()
        new_tags_strlist = tags_str.split(', ') if tags_str else []
        if new_tags_strlist:
            for tag in old_tags:
                if tag.name not in new_tags_strlist:
                    post.tags.remove(tag)
                else:
                    new_tags_strlist.remove(tag.name)

            for tag_name in new_tags_strlist:
                tag_objects = Tag.objects.filter(name=tag_name)
                if tag_objects:
                    tag_object = tag_objects[0]
                else:
                    tag_object = Tag(name=tag_name)
                    tag_object.save()
                post.tags.add(tag_object)
