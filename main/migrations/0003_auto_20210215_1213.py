# Generated by Django 3.1.5 on 2021-02-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_developer_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='description',
        ),
        migrations.AddField(
            model_name='developer',
            name='data',
            field=models.JSONField(default={}),
        ),
    ]
