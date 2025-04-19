import json
from django.shortcuts import render
from books.models import Books


def home_page(request):
    template = 'books/home_page.html'
    context = {}
    return render(request, template, context) 

def create_library(request):
    template = 'books/create_library.html'
    with open('fixtures/books.json', encoding="utf-8") as f:
        library = json.load(f)
    lib = []
    for book in library:
        if (
            Books.objects.filter(name=book['name']).exists() and
            Books.objects.filter(author=book['author']).exists()):
            lib.append(f'Книга "{book['name']}" уже есть в библиотеке!')
        else:
            Books.objects.create(**book)
            lib.append(f'Книга "{book['name']}" сохранена в библиотеке!')
    context = {"availability": lib}
    return render(request, template, context)

def books_view(request):
    books = Books.objects.order_by('pub_date')
    template = 'books/catalog.html'
    context = {'books': books}
    return render(request, template, context)

def show_book(request, slug):
    book = Books.objects.get(slug=slug)
    template = 'books/show_book.html'
    context = {'book': book}
    return render(request, template, context)



