from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    #return "hello world" this wont work
    return HttpResponse("Hello World")
