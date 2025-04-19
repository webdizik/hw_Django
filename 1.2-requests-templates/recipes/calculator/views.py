from django.shortcuts import render

DATA = {
    'omelette': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'beefsteak': {
        'Вырезка говяжья, г': 500,
        'Масло растительное, ст. ложка': 3,
        'Соль,ч. ложка': 0.5,
        'Перец черный молотый, ч. ложка': 0.25,
    },
    'mulled_wine': {
        'Вино красное сухое, л': 1.5,
        'Сахар, г': 300,
        'Гвоздика, шт.': 3,
        'Корица, щепотка': 1,
        'Лимон, шт. (цедра)': 1,
    },
}

def home(request):
    template = 'calculator/home.html'
    return render(request, template)

# В качестве контекста передаётся словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe_view(request, recipe):
    template = 'calculator/index.html'
    context = dict(recipe=DATA.get(recipe))
    return render(request, template, context)


