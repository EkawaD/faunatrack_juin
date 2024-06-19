from django.shortcuts import render
from django.http import HttpResponse

# Class based view
# Class HelloWorld:
# Create your views here.

def hello_world(request):
    return HttpResponse('Hello world!')