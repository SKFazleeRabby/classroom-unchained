import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_active=True, is_teacher=False, is_student=True):
        if not email:
            raise ValueError("An Email is Required for Registration.")
        if not password:
            raise ValueError("You Must Choose a Password.")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.active = is_active
        user.student = is_student
        user.teacher = is_teacher
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, is_active=True, is_teacher=True, is_student=True):
        user = self.create_user(
            email,
            password=password,
            is_student=is_student,
            is_teacher=is_teacher,
            is_active=is_active
        )
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=60, blank=False, null=False)
    hash = models.CharField(max_length=255, null=True)
    teacher = models.BooleanField(default=0)
    student = models.BooleanField(default=0)
    active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_teacher(self):
        return self.teacher

    @property
    def is_student(self):
        return self.student


class UserDetails(models.Model):
    user = models.OneToOneField(User, related_name='details', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(upload_to='profile', default='images/profile_default.jpg')

