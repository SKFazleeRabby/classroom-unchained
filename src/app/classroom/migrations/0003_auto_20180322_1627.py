# Generated by Django 2.0.2 on 2018-03-22 10:27

import app.classroom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20180322_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.CharField(default=app.classroom.models.generate_code, max_length=5),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='id',
            field=models.UUIDField(default='31f54c951cc744ec93ae3bbef94bf86c', editable=False, primary_key=True, serialize=False),
        ),
    ]