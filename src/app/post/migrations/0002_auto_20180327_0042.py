# Generated by Django 2.0.2 on 2018-03-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='094757c42b384a5e8116e15984a61276', editable=False, primary_key=True, serialize=False),
        ),
    ]