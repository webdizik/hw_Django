from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request) -> HttpResponse:
    current_time = datetime.now().now().strftime("%d-%m-%Y %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request) -> HttpResponse:
    dir = ', '.join(os.listdir(path='.'))
    resp = f'Содержимое рабочей директории: {dir}'
    return HttpResponse(resp)
    # raise NotImplemented
