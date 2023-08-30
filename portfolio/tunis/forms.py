from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FeedBack
#
# # Регистрация
#
#
# class FeedBackForm(UserCreationForm):
#     name = forms.CharField(label='Логин', widget=forms.CharField(attrs={'class': 'col-12 col-md-4',
#                                                                             'placeholder': 'Ваше имя',
#                                                                             'required': 'Your Name is Required'}))
#     mail = forms.CharField(label='Пароль', widget=forms.CharField(attrs={'class': 'col-12 col-md-4',
#                                                                               'placeholder': 'Ваш Email'}))
#     company = forms.CharField(label='Повтор пароля', widget=forms.CharField(attrs={'class': 'col-12 col-md-4',
#                                                                                      'placeholder': 'Компания'}))
#     message = forms.CharField(label='Имя', widget=forms.Textarea(attrs={'class': 'col-12',
#                                                                            'placeholder': 'Отправьте мне сообщение и я обязательно с Вами свяжусь"',
#                                                                         }))
#
#     class Meta:
#         model = FeedBack
#         fields = ('name', 'mail', 'company', 'message')
#
#
#


class AddFeedBackForm(forms.Form):
    name = forms.CharField(max_length=155, label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    mail = forms.EmailField(max_length=155, label='Почта', widget=forms.EmailInput(attrs={'placeholder': 'Ваша почта'}))
    company = forms.CharField(max_length=155, label='Компания', widget=forms.TextInput(attrs={'placeholder': 'Компания'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Отправьте мне сообщение и я обязательно с Вами свяжусь'}), label='Сообщение', )
