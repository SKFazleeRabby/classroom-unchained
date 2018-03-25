from django.utils import timezone
from rest_framework_jwt.settings import api_settings
from app.account.serializers import AuthenticatedUserSerializer


def jwt_response_payload_handler(token,  user=None, request=None):
    return {
        'token': token,
        'user': AuthenticatedUserSerializer(user, context={'request': request}).data,
        'exp': timezone.localtime(timezone.now()) + api_settings.JWT_EXPIRATION_DELTA
    }
