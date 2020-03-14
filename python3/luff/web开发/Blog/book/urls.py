from django.urls import path, re_path

from book import views

urlpatterns = [
    re_path('books_info/', views.book_info, name='book_info'),
]
