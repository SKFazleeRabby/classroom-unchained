import random
import uuid
from django.db import models

from app.account.models import User


def generate_code():
    return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz'
                                                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                                 '0123456789') for _ in range(7)])


class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    code = models.CharField(max_length=5, default=generate_code)
    teacher = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.id)


class Lecture(models.Model):
    title = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, related_name='lectures', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.id)


class Content(models.Model):
    content = models.FileField()
    lecture = models.ForeignKey(Lecture, related_name='content', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

