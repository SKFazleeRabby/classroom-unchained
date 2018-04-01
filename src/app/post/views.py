from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from app.post.models import Comment, Post
from app.post.serializers import PostSerializer, CommentSerializer


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            classroom_id=self.kwargs.get('classroom'),
            lecture_id=self.kwargs.get('lecture')
        )


class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(classroom_id=self.kwargs.get('classroom')).select_related('user') \
            .select_related('lecture').prefetch_related('comments')


class DeletePostAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        return Post.objects.filter(classroom_id=self.kwargs.get('classroom')).filter(user=self.request.user)


class CreateCommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            post_id=self.kwargs.get('post')
        )


class DeleteCommentAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user).filter(post_id=self.kwargs.get('post'))
