from django.urls import path
#path is a function to define URL patterns

from . import views

urlpatterns = [ #this will be list
    path('', views.home, name='home') 
    #but we dont have this funciton
    #since this is home page dont metion / or anything like that
    #path takes two arguments 1) url patter 2) a view function that is called when url is matched
    #in django we can assign a name to each url pattern
]