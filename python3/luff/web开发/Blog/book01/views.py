from django.shortcuts import render, HttpResponse, redirect, reverse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import json

from book01.models import Author, AuthorDetail, Publish, Book, PageDemo, User
from book01.forms import UserReg

# Create your views here.


def add_book(request):
    if request.method == 'GET':
        publish_obj = Publish.objects.all().values('id', 'name')
        author_obj = Author.objects.all().values('id', 'name')
        return render(request, 'book01/add_book.html',
                      {'publishes': publish_obj, 'authors': author_obj})
    if request.method == 'POST':
        publish_obj = Publish.objects.get(id=request.POST.get('publish_list'))
        authors_obj = Author.objects.filter(
            id__in=[int(nid) for nid in request.POST.getlist('author_list')]
        )
        print(authors_obj)
        book_obj = Book.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            pub_date=request.POST.get('pub_date'),
            publish=publish_obj,
        )
        book_obj.authors.add(*authors_obj)

        return redirect(reverse('book01:book_info'))


def book_info(request):
    books_info = Book.objects.all()
    return render(request, 'book01/book_info.html', {'books_info': books_info})


def add_author(request):
    if request.method == 'GET':
        return render(request, 'book01/add_author.html')
    if request.method == 'POST':
        author_detail_obj = AuthorDetail.objects.create(
            age=request.POST.get('age'),
            telephone=request.POST.get('telephone'),
            addr=request.POST.get('addr'),
            birthday=request.POST.get('birthday'),
        )
        Author.objects.create(
            name=request.POST.get('name'),
            author_detail=author_detail_obj,
        )
        return HttpResponse('添加成功')


def add_publish(request):
    if request.method == 'GET':
        return render(request, 'book01/add_publish.html')
    if request.method == 'POST':
        print(request.POST)
        Publish.objects.create(
            name=request.POST.get('name'),
            city=request.POST.get('city'),
            email=request.POST.get('email'),
        )
        # result = {"resCode": '0', "message": 'success', "data": []}
        publish_obj = Publish.objects.all()
        ret = serializers.serialize('json', publish_obj)

        return HttpResponse(ret, content_type='application/json')


def delete_book(request, book_id):
    book_obj = Book.objects.filter(id=book_id).delete()
    return redirect(reverse('book01:book_info'))


def edit_book(request, book_id):
    if request.method == 'GET':
        book_obj = Book.objects.filter(id=book_id)[0]
        publish_obj = Publish.objects.all()
        author_obj = Author.objects.all()

        return render(request, 'book01/edit_book.html', {
            'book_info': book_obj, 'publishes': publish_obj, 'authors': author_obj
        })
    if request.method == 'POST':
        book_obj = Book.objects.get(id=book_id)
        publish_obj = Publish.objects.get(id=request.POST.get('publish_list'))
        author_obj = Author.objects.filter(
            id__in=[int(nid) for nid in request.POST.getlist('author_list')]
        )
        edit_book_obj = Book.objects.filter(id=book_id).update(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            pub_date=request.POST.get('pub_date'),
            publish=publish_obj,
        )
        print(edit_book_obj)
        book_obj.authors.clear()
        book_obj.authors.add(*author_obj)

        return redirect(reverse('book01:book_info'))


def file_upload(request):
    if request.method == 'POST':
        json_obj = request.body
        print(json_obj)
        file_obj = request.FILES.get('img')
        print(file_obj)
        with open(file_obj.name, 'wb') as f:
            for line in file_obj:
                f.write(line)

        return HttpResponse('上传成功')
    return render(request, 'book01/file_upload.html')


def page_demo(request):
    # book_list = []
    # for i in range(1000):
        # book_obj = PageDemo(
            # name='book_%s' % i, price=i * i
        # )
        # book_list.append(book_obj)
    # PageDemo.objects.bulk_create(book_list)
    book_list = PageDemo.objects.all()
    panitor = Paginator(book_list, 10)
    # print(panitor.count)
    # print(panitor.num_pages)
    # print(panitor.page_range)
    current_page_num = int(request.GET.get('page', 1))
    show_page_num = 11
    if panitor.num_pages < show_page_num:
        page_range = panitor.page_range
    else:
        if current_page_num < show_page_num/2:
            page_range = range(1, show_page_num+1)
        elif current_page_num > panitor.num_pages-int(show_page_num/2):
            page_range = range(panitor.num_pages-show_page_num+1, panitor.num_pages+1)
        else:
            page_range = range(current_page_num-int(show_page_num/2), current_page_num+int(show_page_num/2)+1)

    try:
        page_content = panitor.page(current_page_num)
        # print(page_content.object_list)
    except EmptyPage as e:
        current_page_num = 1
        page_content = panitor.page(current_page_num)
    return render(request, 'book01/page_demo.html', {
        'book_list': page_content, 'current_page_num': current_page_num, 'page_range': page_range
    })


def reg(request):
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            return HttpResponse('ok')
        else:
            print(form.errors)
            password_diff_err = form.errors.get('__all__')
            return render(request, 'book01/reg.html', locals())
    form = UserReg()
    return render(request, 'book01/reg.html', locals())


def session_login(request):
    if request.method == 'POST':
        user_obj = User.objects.filter(name=request.POST.get('user'), password=request.POST.get('pwd')).first()
        if user_obj:
            # ret = HttpResponse('登录成功')
            # ret.set_cookie('name', request.POST.get('user'))
            # import datetime
            # date = datetime.datetime(year=2020, month=3, day=30, hour=16, minute=18, second=0)
            # ret.set_cookie('is_login', True, path='/book01/test')
            request.session['is_login'] = True
            return HttpResponse('登录成功')
        else:
            return render(request, 'book01/session_login.html')
    return render(request, 'book01/session_login.html')


def session_index(request):
    if request.COOKIES.get('name'):
        return render(request, 'book01/session_index.html')
    else:
        return redirect(reverse('book01:session_login'))


def session_test(request):
    print(request.session.get('is_login'))
    return HttpResponse('test')


def session_del(request):
    # del request.session['is_login']
    request.session.flush()
    return HttpResponse('del')


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=username, password=pwd)
        if user:
            auth.login(request, user)
            next_url = request.GET.get('next', reverse('book01:auth_index'))
            return redirect(next_url)
    return render(request, 'book01/session_login.html')


def auth_index(request):
    return render(request, 'book01/session_index.html')


def auth_logout(request):
    auth.logout(request)
    return redirect(reverse('book01:session_login'))


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.models.User.objects.create_user(username=username, password=pwd)
        return redirect(reverse('book01:session_login'))
    return render(request, 'book01/reg.html')
