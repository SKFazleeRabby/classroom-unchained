import uuid
from django.db import models

from app.account.models import User
from app.classroom.models import Classroom, Lecture


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex, editable=False)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, related_name='posts', on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()

