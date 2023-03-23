from django.urls import path
#path is a function to define URL patterns

from . import views

urlpatterns = [ #this will be list
    path('', views.index, name='index'),
]