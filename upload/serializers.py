# -*- coding: utf-8 -*-

import mimetypes

from rest_framework import serializers


class UploadCreateSerializer(serializers.Serializer):
    content_type = serializers.CharField()

    def validate_content_type(self, value):
        if mimetypes.guess_extension(value) is None:
            raise serializers.ValidationError('content_type is invalid')
        return value


class UploadSerializer(serializers.Serializer):
    token = serializers.CharField()
    key = serializers.CharField()
    bucket_name = serializers.CharField()
