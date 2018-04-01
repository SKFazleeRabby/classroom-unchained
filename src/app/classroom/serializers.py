from rest_framework import serializers
from app.classroom.models import Classroom, Lecture, Content


class TeacherClassroomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'title', 'description', 'code', 'created_at']
        read_only_fields = ['id', 'created_at', 'code']


class ClassroomDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['title', 'description', 'code', 'created_at']


class CreateLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'created_at']
        read_only_fields = ['created_at']


class UploadContentSerializer(serializers.ModelSerializer):
    content_url = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ['lecture', 'content_url']
        read_only_fields = ['content']
        extra_kwargs = {
            'content_url': {'read-only': True}
        }

    def get_content_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.content.url)


class LecturesSerializers(serializers.ModelSerializer):
    content = UploadContentSerializer(read_only=True, many=True)

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'description', 'created_at', 'content']
        read_only_fields = ['id', 'content', 'created_at']


class ListLecturesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title']
