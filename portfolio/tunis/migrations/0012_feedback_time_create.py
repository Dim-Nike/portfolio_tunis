# Generated by Django 4.1.4 on 2023-05-18 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tunis', '0011_feedback_userself_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
    ]
