from rest_framework import serializers
from app.account.models import User, UserDetails


class UserDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = UserDetails
        fields = ['first_name', 'last_name', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)


class AuthenticatedUserSerializer(serializers.ModelSerializer):
    details = UserDetailSerializer(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'is_teacher', 'is_student', 'details']


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(label='First Name', max_length=30, allow_blank=False)
    last_name = serializers.CharField(label='Last Name', max_length=30, allow_blank=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email')
        )
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.set_password(validated_data.get('password'))
        user.save()
        return user
