from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>home page</h1>')

def about(request):
    return HttpResponse('<h1>about page</h1>')


def gallery(request):
    return HttpResponse('<h1>gallery page</h1>')