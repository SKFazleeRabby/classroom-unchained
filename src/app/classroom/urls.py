from django.urls import path
from app.classroom.views import (
    CreateClassroomAPIView,
    ListClassroomAPIView,
    CreateLecturesAPIView,
    UploadContentAPIView,
    AllLecturesAPIView, ClassroomDetailsAPIView, ListLecturesAPIView)

app_name = 'classroom'

urlpatterns = [
    path('create/', CreateClassroomAPIView.as_view(), name='create-classroom'),
    path('all/', ListClassroomAPIView.as_view(), name='all-classroom'),
    path('<uuid:classroom>/', ClassroomDetailsAPIView.as_view(), name='classroom-detail'),
    path('<uuid:classroom>/lecture/create/', CreateLecturesAPIView.as_view(), name='create-lectures'),
    path('lecture/content/upload/', UploadContentAPIView.as_view(), name='upload-contents'),
    path('<uuid:classroom>/lecture/', AllLecturesAPIView.as_view(), name='all-lectures'),
    path('<uuid:classroom>/lecture/list/', ListLecturesAPIView.as_view(), name='list-lecture')
]
