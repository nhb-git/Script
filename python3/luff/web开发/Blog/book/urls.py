from django.urls import path, re_path

from book import views

urlpatterns = [
    re_path('books_info/', views.book_info, name='book_info'),
    re_path('add_book/', views.add_book, name='add_book'),
    re_path(r'delete/(?P<book_id>\d+)/book/', views.delete_book, name='delete_book'),
    re_path(r'edit/(?P<book_id>\d+)/book/', views.edit_book, name='edit_book'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('delete/', views.delete, name='delete'),
]
