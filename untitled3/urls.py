from django.contrib import admin
from django.urls import path, include

from untitled3.views import show_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main_page),
    path('', include('books.urls')),
    path('', include('categories.urls')),

]