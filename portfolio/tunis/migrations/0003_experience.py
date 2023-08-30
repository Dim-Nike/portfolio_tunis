# Generated by Django 4.2.1 on 2023-05-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunis', '0002_alter_progress_is_active_alter_skills_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_exp', models.CharField(choices=[('1', 'Коммерческий опыт'), ('2', 'Обучение')], max_length=1, verbose_name='Тип опыта')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('dsc', models.CharField(max_length=255, verbose_name='Описание(255 символов)')),
            ],
            options={
                'verbose_name': 'Опыт',
                'verbose_name_plural': 'Опыты',
            },
        ),
    ]
