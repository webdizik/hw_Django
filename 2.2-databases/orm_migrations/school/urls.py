from django.urls import path

from school.views import students_list, teachers_list

urlpatterns = [
    path('students', students_list, name='students'),
    path('teachers', teachers_list, name='teachers'),
]
