from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(requet):
    #return "hello world" this wont work
    return HttpResponse("Hello World")
