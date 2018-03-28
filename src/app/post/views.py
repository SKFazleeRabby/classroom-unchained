from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.classroom.models import Classroom, Lecture
from app.post.models import Comment, Post
from app.post.serializers import PostSerializer


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            classroom_id=self.kwargs.get('classroom'),
            lecture_id=self.kwargs.get('lecture')
        )


class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return Post.objects.filter(classroom_id=self.kwargs.get('classroom'))

