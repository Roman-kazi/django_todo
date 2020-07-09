from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html")
# often times we will have urls.py for each app in the project

def roman(request):
    return HttpResponse("Roman")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })
