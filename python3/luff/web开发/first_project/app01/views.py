from django.shortcuts import render

# Create your views here.
import time


def timer(request):
    current_time = time.time()
    return render(request, "timer.html", {"current_time": current_time})
