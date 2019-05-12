from django.shortcuts import HttpResponse
from categories.models import Category

def show_categories(request):
    categories = Category.objects.all()
    result = ''

    for category in categories:
        result += f'<a href = "http://127.0.0.1:8000/categories/{category.id}/">{category.name}</a><br>'
    return HttpResponse(result)

def show_category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    result = f'Название:{category.name} - Фантастический жанр, повествующий о выдуманных событиях.'
    books = category.books.all()
    return HttpResponse(result)