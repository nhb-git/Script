from django.shortcuts import render, HttpResponse, reverse
from blogs.models import Book
# Create your views here.


def login(request):
    # return HttpResponse(reverse("blogs:login"))
    return render(request, 'blogs/login.html')


def get_year(request, year):
    return HttpResponse(reverse('blogs:get_year', args=(year,)))


def get_month(request, month):
    print(month)
    print(type(month))
    return HttpResponse(reverse("blogs:get_month", args=(month,)))


def get_name_age(request):
    import datetime
    now = datetime.datetime.now()
    file_size = 123233232
    text = 'test xxxiyyy zzz lll sss nnn mmm'
    a_link = '<a href="#">123</a>'
    a = 30
    return render(request, 'blogs/get_name_age.html', {"test": [1, 2], "now": now, "file_size": file_size,
                                                       "text": text, "a_link": a_link, "a": a})


def show_detail(request):
    return render(request, 'blogs/detail.html')


def add_book_info(request):
    # book_obj = Book(id=1, title='白鹿原', pub_date='2020-03-10', price=100, publish='人民出版社')
    # 返回值是这条记录
    book_obj = Book.objects.create(title='php', pub_date='2021-03-10', price=101, publish='人民出版社')
    print(book_obj.title)
    return HttpResponse('add success.')


def search_book(request):
    # all()方法被管理器调用，返回QuerySet对象
    # books_obj = Book.objects.all()
    # print(books_obj)
    # print(books_obj[0])
    # first()/last()的调用者是QuerySet对象, 返回值是model对象
    # print(books_obj.first())
    # print(books_obj.last())
    # filter()方法的调用者是管理器，返回值是QuerySet对象
    # books_obj = Book.objects.filter(price=100)
    # books_obj = Book.objects.filter(title='php', price=100)
    # books_obj = Book.objects.exclude(price=100)
    books_obj = Book.objects.all().order_by('-id')
    # books_obj = Book.objects.all().order_by('id', 'price')
    # print(books_obj)
    # print(books_obj.count())
    # print(books_obj.exists())
    # print(books_obj.values('price', 'id'))
    # print(books_obj.values_list('price', 'id'))
    # print(books_obj.values('price').distinct())
    # print(books_obj.filter(price__gt=100, price__lt=102))
    # print(books_obj.filter(title__startswith='go'))
    # print(books_obj.filter(title__icontains='h'))
    # print(books_obj.filter(title__in=['goH', 'y'])))
    print(books_obj.filter(pub_date__year='2021'))
    return HttpResponse('search book')


def delete_book_info(request):
    book_obj = Book.objects.filter(price=103).update(title='Python')

    return HttpResponse('delete success')
