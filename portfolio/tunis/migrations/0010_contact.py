# Generated by Django 4.2.1 on 2023-05-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunis', '0009_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_link', models.CharField(max_length=155, verbose_name='Ссылка вк')),
                ('tg_link', models.CharField(max_length=155, verbose_name='Ссылка телеграмм')),
                ('WhatsApp_link', models.CharField(max_length=155, verbose_name='Ссылка WhatsApp')),
                ('gitHub_link', models.CharField(max_length=155, verbose_name='Ссылка GitHub')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
