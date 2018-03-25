from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.account.models import User
from app.classroom.models import Classroom, Lecture, Content
from app.classroom.serializers import (
    CreateClassroomSerializers,
    TeacherClassroomListSerializers,
    CreateLectureSerializer,
    UploadContentSerializer
)


# User.objects.get(id='3b911785-b421-4d0b-9c0f-02014170fa78')


class CreateClassroomAPIView(CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = CreateClassroomSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ListClassroomAPIView(ListAPIView):
    serializer_class = TeacherClassroomListSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return Classroom.objects.filter(teacher=self.request.user)


class CreateLecturesAPIView(CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = CreateLectureSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


class UploadContentAPIView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = UploadContentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
