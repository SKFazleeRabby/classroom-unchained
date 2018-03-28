import random
import uuid

import os
from django.db import models

from app.account.models import User


def generate_code():
    return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz'
                                                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                                 '0123456789') for _ in range(7)])


def hex_uid():
    return uuid.uuid4().hex


class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, default=hex_uid, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    code = models.CharField(max_length=7, default=generate_code)
    teacher = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} ({})'.format(self.title, self.id)


class Lecture(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='adaknaskjvnakjvnkjsgnkjgnkjsgnkjsgnkjsgnkjsdgnksjgnskgjn')
    classroom = models.ForeignKey(Classroom, related_name='lectures', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} ({})'.format(self.title, self.id)


class Content(models.Model):

    def upload_path(self, filename):
        return 'lectures/' + str(self.lecture.classroom_id) + '/' \
               + str(self.lecture_id) + '/' + '/' + filename

    content = models.FileField(upload_to=upload_path)
    lecture = models.ForeignKey(Lecture, related_name='content', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

