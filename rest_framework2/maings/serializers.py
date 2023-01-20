from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =(
            'id', 'name', 'user',
        )
        read_only_fields = ('user',)

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many = True)
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'posts',
        )