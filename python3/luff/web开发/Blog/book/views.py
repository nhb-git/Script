from django.shortcuts import render
from book.models import Book

# Create your views here.


def book_info(request):
    books_info = []
    books_obj = Book.objects.all()
    books_info = books_obj.values('title', 'price', 'pub_date', 'publish')
    return render(request, 'book/books_info.html', {'books_info': books_info})
