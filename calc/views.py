from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    #return "hello world" this wont work
    #return HttpResponse("Hello World")
    #return HttpResponse("<h1>Hello World</h1>") this will work
    #return render(request,'home.html') #this home.html is in templates folder 
    return render(request,'home.html',{'name':'anirudh'})
