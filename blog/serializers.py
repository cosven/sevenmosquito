from rest_framework import serializers
from .models import Post


class BlogSearchSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')


class SearchSerializer(serializers.Serializer):
    posts = BlogSearchSummarySerializer(many=True)
