from django.urls import path
from app.classroom.views import (
    CreateClassroomAPIView,
    ListClassroomAPIView,
    CreateLecturesAPIView,
    UploadContentAPIView
)

app_name = 'classroom'

urlpatterns = [
    path('create/', CreateClassroomAPIView.as_view(), name='create-classroom'),
    path('all/', ListClassroomAPIView.as_view(), name='all-classroom'),
    path('lecture/create', CreateLecturesAPIView.as_view(), name='create-lectures'),
    path('lecture/content/upload', UploadContentAPIView.as_view(), name='upload-contents')
]
