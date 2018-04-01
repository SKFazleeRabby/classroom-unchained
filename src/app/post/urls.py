from django.urls import path
from app.post.views import CreatePostAPIView, ListPostAPIView, CreateCommentAPIView, ListCommentAPIView

app_name = 'post'

urlpatterns = [
    path('<uuid:classroom>/<int:lecture>/post/', CreatePostAPIView.as_view(), name='create-post'),
    path('<uuid:classroom>/post/', ListPostAPIView.as_view(), name='list-post'),
    path('<uuid:post>/comment/', CreateCommentAPIView.as_view(), name='create-comment')
]
