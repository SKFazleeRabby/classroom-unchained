# Generated by Django 2.0.2 on 2018-03-26 18:35

import app.classroom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20180325_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='id',
            field=models.UUIDField(default='7c5b85dffcde453dbeadbe928d6b2303', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.FileField(upload_to=app.classroom.models.Content.upload_path),
        ),
    ]