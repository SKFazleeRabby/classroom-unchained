# Generated by Django 2.0.2 on 2018-03-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20180328_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='449c6741ffed455f8bbd9da32a60bb4e', editable=False, primary_key=True, serialize=False),
        ),
    ]
