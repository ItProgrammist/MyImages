from django.http import HttpResponse

from books.models import Book
from categories.models import Category


def show_books(request):
    books = Book.objects.all()
    result = ''

    for book in books:
        result += f'<a href = "/books/{book.id}/">{book.name}</a>'
    return HttpResponse(result)

def show_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    result = f'Название:{book.name}<br>Категория:{book.category.name}<br>Цена:{book.price}<br>Описание:{book.description}'
    return HttpResponse(result)