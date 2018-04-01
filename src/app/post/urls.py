from django.urls import path
from app.post.views import (
    CreatePostAPIView,
    ListPostAPIView,
    CreateCommentAPIView,
    DeletePostAPIView,
    DeleteCommentAPIView
)

app_name = 'post'

urlpatterns = [
    path('<uuid:classroom>/<int:lecture>/post/', CreatePostAPIView.as_view(), name='create-post'),
    path('<uuid:classroom>/post/', ListPostAPIView.as_view(), name='list-post'),
    path('<uuid:classroom>/<uuid:post_id>/delete/', DeletePostAPIView.as_view(), name='delete-post'),
    path('<uuid:post>/comment/', CreateCommentAPIView.as_view(), name='create-comment'),
    path('<uuid:post>/<int:comment_id>/delete/', DeleteCommentAPIView.as_view(), name='delete-comment')
]
