from rest_framework import serializers
from .models import Post, Category, Tag


class BlogSearchSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')


class SearchSerializer(serializers.Serializer):
    posts = BlogSearchSummarySerializer(many=True)


class BlogUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    tags = serializers.CharField(required=False, allow_blank=True)
    category = serializers.IntegerField(required=False, allow_null=True)

    def update(self, post, validated_data):
        post.title = validated_data.get('title', post.title)
        post.body = validated_data.get('body', post.body)
        category_id = validated_data.get('category')
        if category_id is not None:
            category = Category.objects.get(id=category_id)
            post.category = category
        tags_str = validated_data.get('tags')
        if tags_str is not None:
            tags_str = tags_str.strip()
            old_tags = post.tags.all()
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
        post.save()
        return post
