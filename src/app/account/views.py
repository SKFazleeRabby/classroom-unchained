from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from app.account.models import User
from app.account.serializers import TeacherRegistrationSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TeacherRegistrationAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherRegistrationSerializer

