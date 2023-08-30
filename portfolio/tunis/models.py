from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserSelf(models.Model):
    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    name = models.CharField(verbose_name='Имя', max_length=155)
    surname = models.CharField(verbose_name='Фамилия', max_length=155)
    age = models.IntegerField(verbose_name='Возраст')
    dsc = models.TextField(verbose_name='Описание о себе')
    photo_desktop = models.ImageField(verbose_name='Фотография(610х1020)',  upload_to='photo/desktop/%Y/%m/%d/')
    photo_mobile = models.ImageField(verbose_name='Фотография(300х300)', upload_to='photo/mobile/%Y/%m/%d/')
    work_experience = models.IntegerField(verbose_name='Стаж работы')
    address = models.CharField(verbose_name='Адрес', max_length=155)
    phone = models.CharField(verbose_name='Номер телефона', max_length=155)
    mail = models.EmailField(verbose_name='Почта')
    education = models.CharField(verbose_name='Образование', max_length=255)
    vacancy = models.CharField(verbose_name='Вакансия', max_length=255)
    resume = models.FileField(verbose_name='Резюме(pdf)', upload_to='photo/resume/%Y/%m/%d/')
    salary = models.IntegerField(verbose_name='Желаемая зарплата')
    is_active = models.BooleanField(verbose_name='Активно')


class Progress(models.Model):
    class Meta:
        verbose_name = 'Достижение(не более 4)'
        verbose_name_plural = 'Достижения(не более 4)'

    number = models.IntegerField(verbose_name='Числовое значение')
    progress = models.CharField(verbose_name='Прогресс', max_length=35)
    is_active = models.BooleanField(verbose_name='Активно', default=True)


class Skills(models.Model):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    name = models.CharField(verbose_name='Наименование навыка', max_length=20)
    percentage = models.IntegerField(verbose_name='Усвоение навыка(%)', validators=[MinValueValidator(1),
                                                                                    MaxValueValidator(100)])

    is_active = models.BooleanField(verbose_name='Активно', default=True)


class Experience(models.Model):
    class Meta:
        verbose_name = 'Дорожная карта'
        verbose_name_plural = 'Дорожные карты'

    CHOOSE_TYPE = [('1', 'Коммерческий опыт'),
                   ('2', 'Обучение')]

    type_exp = models.CharField(verbose_name='Тип опыта', max_length=1, choices=CHOOSE_TYPE)
    year = models.IntegerField(verbose_name='Год')
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    dsc = models.CharField(verbose_name='Описание(300 символов)', max_length=300)
    is_active = models.BooleanField(verbose_name='Активно', default=True)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    vk_link = models.CharField(verbose_name='Ссылка вк', max_length=155)
    tg_link = models.CharField(verbose_name='Ссылка телеграмм', max_length=155)
    WhatsApp_link = models.CharField(verbose_name='Ссылка WhatsApp', max_length=155)
    gitHub_link = models.CharField(verbose_name='Ссылка GitHub', max_length=155)
    is_active = models.BooleanField(verbose_name='Активно', default=True)


class FeedBack(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    name = models.CharField(verbose_name='Имя', max_length=155)
    mail = models.CharField(verbose_name='Почта', max_length=155)
    company = models.CharField(verbose_name='Компания', max_length=155)
    message = models.TextField(verbose_name='Сообщение')
    time_create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)


class Role(models.Model):
    class Meta:
        verbose_name = 'Роль в проекте'
        verbose_name_plural = 'Роли в проекте'

    name = models.CharField(verbose_name=' Название', max_length=255)

    def __str__(self):
        return self.name


class TypeProject(models.Model):
    class Meta:
        verbose_name = 'Тип проекта'
        verbose_name_plural = 'Типы в проектах'

    name = models.CharField(verbose_name='Тип', max_length=155)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    name = models.CharField(verbose_name='Наименование', max_length=50)
    full_name = models.CharField(verbose_name='Полное название', max_length=255)
    type_project = models.ForeignKey(TypeProject, verbose_name='Тип проекта', on_delete=models.PROTECT)
    photo_logo = models.ImageField(verbose_name='Фотография лого', upload_to='photo/project/logo/%Y/%m/%d/')
    stack = models.CharField(verbose_name='Стек технологий', max_length=155)
    photo_preview = models.ImageField(verbose_name='Фотография превью', upload_to='photo/project/preview/%Y/%m/%d/')
    photo = models.ImageField(verbose_name='Фотография проекта', upload_to='photo/project/dsc/%Y/%m/%d/')
    preview = models.CharField(verbose_name='Ссылка на проект', max_length=255)
    role = models.ForeignKey(Role, verbose_name='Роль', on_delete=models.PROTECT)
    time = models.DateTimeField(verbose_name='Дата выполнения')
    dsc = models.TextField(verbose_name='Описание проекта')