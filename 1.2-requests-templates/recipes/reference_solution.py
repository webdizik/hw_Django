# Рецепты
# urls.py
from django.urls import path
from calculator.views import recipes

urlpatterns = [
    path('<str:name>/', recipes)
]
