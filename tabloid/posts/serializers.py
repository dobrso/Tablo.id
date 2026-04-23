from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tag, Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']

class PostSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'tags', 'author']
