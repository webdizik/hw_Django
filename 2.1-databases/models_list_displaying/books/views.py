import json
from django.shortcuts import render
from django.core.paginator import Paginator

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

def show_book_name(request, slug):
    template = 'books/show_book_name.html'
    
    books = Books.objects.order_by('pub_date')
    book = Books.objects.get(slug=slug)

    current_page = request.GET.get('page', 1)
    paginator = Paginator(books, 1)
    page = paginator.get_page(current_page)
    print(page)
    context = {'book': book, 'page': page}

    return render(request, template, context)

def show_book_pub_date(request, pub_date):
    books = Books.objects.order_by('pub_date')
    book = Books.objects.get(pub_date=pub_date)
    
    current_page = book.id
    paginator = Paginator(books, 1)
    page = paginator.get_page(current_page)
    
    template = 'books/show_book_pub_date.html'
    context = {'book': book, 'page': page}
    
    return render(request, template, context)
