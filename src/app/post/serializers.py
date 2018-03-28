from rest_framework import serializers

from app.post.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['content', 'user', 'classroom', 'lecture', 'created_at']
        read_only_fields = ['user', 'classroom', 'lecture', 'created_at']

