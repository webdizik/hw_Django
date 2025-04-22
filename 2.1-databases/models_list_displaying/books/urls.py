from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('books/', views.books_view, name='books'),
    path('create_db/', views.create_library, name='db'),
    path('books/<slug:slug>/', views.show_book_name, name='show_book_name'),
    path('books/<slug:pub_date>/', views.show_book_pub_date, name='show_book_pub_date'),
]