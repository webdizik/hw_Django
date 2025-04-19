from django.contrib import admin

from books.models import Books


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date', 'image')


admin.site.register(Books, BookAdmin)
