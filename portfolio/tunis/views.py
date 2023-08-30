from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import AddFeedBackForm


# from .forms import FeedBackForm


def show_index(req):
    data = {
        'title': 'Главная страница',
        'users': UserSelf.objects.filter(is_active=True)
    }
    return render(request=req, template_name='tunis/dark/index.html', context=data)


def show_about(req):
    data = {
        'title': 'О себе',
        'users': UserSelf.objects.filter(is_active=True),
        'progresses': Progress.objects.filter(is_active=True),
        'skills': Skills.objects.filter(is_active=True),
        'educations': Experience.objects.filter(type_exp='2', is_active=True).order_by('year'),
        'commercials': Experience.objects.filter(type_exp='1', is_active=True).order_by('year'),
    }

    return render(req, 'tunis/dark/about.html', data)


def show_portfolio(req):
    data = {
        'projects': Project.objects.all(),
        'title': 'Мои проекты'
    }

    return render(req, 'tunis/dark/portfolio.html', data)


def show_detail_project(req, pk):
    data = {
        'projects': Project.objects.filter(pk=pk)
    }

    return render(req, 'tunis/dark/blog-post.html', data)


def show_contact(req):
    btn_msg = 'Отправить'
    if req.method == 'POST':

        form = AddFeedBackForm(req.POST)
        if form.is_valid():
            try:
                FeedBack.objects.create(**form.cleaned_data)
                btn_msg = 'Спасибо за обращение!'
                return redirect('about')
            except:
                print(f'Ошибка добавления формы записи')
    else:
        form = AddFeedBackForm()

    data = {
        'title': 'Мои контакты',
        'users': UserSelf.objects.filter(is_active=True),
        'contacts': Contact.objects.filter(is_active=True),
        'form': form,
        'btn_msg': btn_msg
        # 'form': FeedBackForm(req.POST)

    }
    return render(req, 'tunis/dark/contact.html', data)
