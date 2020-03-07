from django.shortcuts import render, HttpResponse, reverse

# Create your views here.


def login(request):
    # return HttpResponse(reverse("blogs:login"))
    return render(request, 'blogs/login.html')
