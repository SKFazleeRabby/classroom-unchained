from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from app.classroom.models import Classroom, Lecture, Content
from app.classroom.serializers import (
    TeacherClassroomListSerializers,
    UploadContentSerializer,
    LecturesSerializers, ClassroomDetailsSerializers,
    ListLecturesSerializers)


class CreateClassroomAPIView(CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = TeacherClassroomListSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ListClassroomAPIView(ListAPIView):
    serializer_class = TeacherClassroomListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Classroom.objects.filter(teacher=self.request.user)


class ClassroomDetailsAPIView(RetrieveAPIView):
    serializer_class = ClassroomDetailsSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom'

    def get_queryset(self):
        return Classroom.objects.filter(teacher=self.request.user)


class CreateLecturesAPIView(CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LecturesSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(classroom_id=self.kwargs.get('classroom'))


class AllLecturesAPIView(ListAPIView):
    serializer_class = LecturesSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lecture.objects.filter(classroom_id=self.kwargs.get('classroom')).prefetch_related('content')


class ListLecturesAPIView(ListAPIView):
    serializer_class = ListLecturesSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lecture.objects.filter(classroom_id=self.kwargs.get('classroom')).order_by('created_at') \
            .only('id', 'title')


class UploadContentAPIView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = UploadContentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(content=self.request.data.get('file'))
