# Generated by Django 3.0.8 on 2020-08-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200803_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.ManyToManyField(to='api.User'),
        ),
    ]
