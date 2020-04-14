from django.shortcuts import render, HttpResponse, reverse, redirect
from django.db.models import Avg, Max, Min, Count, F, Q
from book.models import Book, Publish, Author, AuthorDetail

# Create your views here.


def book_info(request):
    books_info = []
    books_obj = Book.objects.all()
    books_info = books_obj.values('id', 'title', 'price', 'pub_date', 'publish')
    return render(request, 'book/books_info.html', {'books_info': books_info})


def add_book(request):
    if request.method == 'POST':
        book_obj = Book.objects.create(
            title=request.POST.get('book_name'),
            pub_date=request.POST.get('pub_date'),
            price=request.POST.get('book_price'),
            publish=request.POST.get('publish')
        )
        return redirect(reverse('book:book_info'))
    return render(request, 'book/add_book.html')


def delete_book(request, book_id):
    book_obj = Book.objects.filter(id=book_id).delete()
    return redirect(reverse('book:book_info'))


def edit_book(request, book_id):
    if request.method == 'GET':
        book_obj = Book.objects.filter(id=book_id)
        book_info = book_obj[0]
        print(book_obj)
        return render(request, 'book/edit_book.html', {'book_info': book_info})
    if request.method == 'POST':
        book_obj = Book.objects.filter(id=book_id).update(
            title=request.POST.get('book_name'),
            price=request.POST.get('book_price'),
            pub_date=request.POST.get('pub_date'),
            publish=request.POST.get('publish')
        )
        return redirect(reverse('book:book_info'))


def add(request):
    # 一对多关系
    ## 添加数据 method 1, 直接在多表的里面给外键赋值另一个1关系的id
    ## publish_obj = Publish.objects.create(name='人民出版社', city='北京', email='renming@163.com')
    ## book_obj = Book.objects.create(title='python', publish_date='2018-01-01', price=100, publish_id=1)

    # 添加数据 method 2，直接在多表的关系里面给外键赋值一个1关系中的对象
    # publish_obj = Publish.objects.filter().last()
    # book_obj = Book.objects.create(
        ## title='go', publish_date='2019-01-01', price=101, publish=publish_obj
    # )
    # print(book_obj.publish)
    # print(book_obj.publish_id)
    author1 = Author.objects.get(name='nhb')
    author2 = Author.objects.get(name='nhb1')
    book_obj = Book.objects.get(title='php')
    print(book_obj)
    book_obj.authors.add(author1, author2)
    return HttpResponse('添加成功')


def search(request):
    # book_obj = Book.objects.filter(title='go').first()
    # publish_name = book_obj.publish.name
    # book_obj = Book.objects.get(title='php')
    # print(book_obj.authors.all())
    # publish_obj = Publish.objects.get(name='人民出版社')
    # print(publish_obj.book_set.all())
    # print(book_obj.authors.all())

    # 一对一正向查询
    # author_obj = Author.objects.get(name='nhb')
    # print(author_obj.author_detail.telephone)

    # 一对一反向查询
    # ad = AuthorDetail.objects.get(telephone=133)
    # print(ad.author.name)

    ################### 基于双下划线的查询（join查询）####################

    # 一对多正向查询
    # ret = Book.objects.filter(title='python').values('publish__name')
    # print(ret)
    # 一对多反向查询
    # ret = Publish.objects.filter(book__title='python').values('name')

    # 多对多正向查询
    # ret = Book.objects.filter(title='php').values('authors__name')

    # 多对多反向查询
    # ret = Author.objects.filter(book__title='php').values('name')

    # 一对一正向查询
    # ret = Author.objects.filter(name='nhb').values('author_detail__telephone')

    # 一对一反向查询
    # ret = AuthorDetail.objects.filter(author__name='nhb')

    # 进阶练习:
    # 查询以1开头的电话的作者所出版过的书籍名称和对应出版社名称
    # ret = Author.objects.filter(author_detail__telephone__startswith=1).values('book__title', 'book__publish__name').distinct()
    # ret = Book.objects.filter(authors__author_detail__telephone__startswith=1).values('title', 'publish__name').distinct()
    # author_detail_obj = AuthorDetail.objects.filter(telephone__startswith='1').first()
    # print(author_detail_obj)
    # author_obj = author_detail_obj.author.name
    # print(author_obj)
    # ret = Book.objects.all().aggregate(min_price=Min('price'), max_price=Max('price'))
    # ret = Publish.objects.values('nid').annotate(c=Count('book__title')).values('name', 'c')
    # ret = Book.objects.filter(comment_num__gt=F('read_num'))
    # print(ret)
    # Book.objects.all().update(price=F('price')+1)
    ret = Book.objects.filter(~Q(title='php') | Q(price='102'))
    print(ret)
    return HttpResponse('查找成功')


def delete(request):
    book_obj = Book.objects.get(title='php')
    author1 = Author.objects.get(name='nhb')
    # book_obj.authors.remove(author1)
    book_obj.authors.clear()
    return HttpResponse('删除成功')
