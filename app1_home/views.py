from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def welcome(Request):
#    return  HttpResponse("<h1 style ='background:hotpink' >Hello! all this is my first Django app <h1>")
    my_dict={"insert_me":"I am coming from the views.py files of the app_1 "}
    return render(Request,"app1_home/Reg.html",context = my_dict)