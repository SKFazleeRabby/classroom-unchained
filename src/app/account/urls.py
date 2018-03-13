from django.urls import path
from app.account.views import TeacherRegistrationAPI


app_name = 'account'

urlpatterns = [
    path('register/', TeacherRegistrationAPI.as_view(), name='user_registration')
]

