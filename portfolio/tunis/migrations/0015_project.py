# Generated by Django 4.1.4 on 2023-05-19 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunis', '0014_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное название')),
                ('photo_logo', models.ImageField(upload_to='photo/project/logo/%Y/%m/%d/', verbose_name='Фотография лого')),
                ('stack', models.CharField(max_length=155, verbose_name='Стек технологий')),
                ('photo_preview', models.ImageField(upload_to='photo/project/preview/%Y/%m/%d/', verbose_name='Фотография превью')),
                ('photo', models.ImageField(upload_to='photo/project/dsc/%Y/%m/%d/', verbose_name='Фотография проекта')),
                ('preview', models.CharField(max_length=255, verbose_name='Ссылка на проект')),
                ('time', models.DateTimeField(verbose_name='Дата выполнения')),
                ('dsc', models.TextField(verbose_name='Описание проекта')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tunis.role', verbose_name='Роль')),
                ('type_project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tunis.typeproject', verbose_name='Тип проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
