from django.shortcuts import render, HttpResponse, reverse

# Create your views here.


def login(request):
    return render(request, 'news/login.html')
