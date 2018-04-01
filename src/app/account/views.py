from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from app.account.models import User
from app.account.serializers import TeacherRegistrationSerializer


class TeacherRegistrationAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherRegistrationSerializer
    permission_classes = [AllowAny]

