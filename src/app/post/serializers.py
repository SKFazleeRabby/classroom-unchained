from rest_framework import serializers

from app.account.models import User
from app.account.serializers import UserDetailSerializer
from app.classroom.models import Lecture
from app.post.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    details = UserDetailSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['details']


class PostLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content']
        read_only_fields = ['id', 'user']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    lecture = PostLectureSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'user', 'lecture', 'comments', 'created_at']
        read_only_fields = ['id', 'user', 'lecture', 'comments', 'created_at']

