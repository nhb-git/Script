from django.shortcuts import render, HttpResponse
from django.urls import reverse

# Create your views here.
import time


def timer(request):
    current_time = time.time()
    return render(request, "timer.html", {"current_time": current_time})


def special_case_2003(request):
    return HttpResponse("special case 2003")


def get_year(request, year):
    return HttpResponse(year)


def login(request):
    if request.method == 'GET':
        print(reverse("login1"))
        return render(request, "login.html")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "12" and password == "12":
            return HttpResponse('login ok')
        else:
            return HttpResponse('用户名或密码错误')
