from rest_framework import serializers

from app.account.models import User
from app.account.serializers import AuthenticatedUserSerializer
from app.classroom.models import Classroom, Lecture, Content


class ClassTeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'id']


class CreateClassroomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ['title', 'description']

    def to_representation(self, instance):
        representation = super(CreateClassroomSerializers, self).to_representation(instance)
        representation['teacher'] = AuthenticatedUserSerializer(instance.teacher, required=True).data
        return representation


class TeacherClassroomListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ['title', 'description', 'code']


class CreateLectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ['title', 'classroom', 'created_at']
        read_only_fields = ['created_at']


class UploadContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['content', 'lecture']

