# Generated by Django 4.2.1 on 2023-05-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunis', '0006_experience_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Дорожная карта',
                'verbose_name_plural': 'Дорожные карты',
            },
        ),
    ]