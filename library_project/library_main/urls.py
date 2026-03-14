from django.contrib import admin
from django.urls import path
from books.views import book_list
from authors.views import author_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list),
    path('authors/', author_list),
]
