import os

from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.classroom.models import Classroom
from config.settings import MEDIA_ROOT


@receiver(post_save, sender=Classroom)
def create_classroom_directory(instance, created, **kwargs):
    if created:
        new_dir = os.path.join(MEDIA_ROOT, slugify(instance.title) + '-' + instance.id)
        os.mkdir(new_dir)


@receiver(post_save, sender=Classroom)
def create_lecture_directory(instance, created, **kwargs):
    if created:
        new_dir = os.path.join(MEDIA_ROOT, slugify(instance.title) + '-' + instance.id)
        os.mkdir(new_dir)

