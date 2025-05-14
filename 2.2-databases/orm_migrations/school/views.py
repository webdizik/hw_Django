from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    context = {
        'students': Student.objects.all(),
        'groups': Student.objects.values('group').distinct().order_by('group'),
    }
    
    return render(request, template, context)

def teachers_list(request):
    template = 'school/teachers_list.html'
    context = {'teachers': Teacher.objects.all().order_by('subject')}

    return render(request, template, context)
