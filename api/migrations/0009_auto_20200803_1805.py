# Generated by Django 3.0.8 on 2020-08-03 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200803_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User', to_field='user_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]
