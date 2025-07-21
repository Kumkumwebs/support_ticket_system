from rest_framework import serializers
from .models import Post, Comment

# ✅ Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'comment', 'created_at']
        read_only_fields = ['user']


# ✅ Post Serializer (without image/video support)
class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'likes', 'comments']
        read_only_fields = ['user']
