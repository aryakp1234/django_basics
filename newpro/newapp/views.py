from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.

def index (request):
    return HttpResponse('<h1>welcome</h1>')

def about(request):
    return HttpResponse('<h1>about us</h1>')

def gallery(request):
    return HttpResponse('<h1>wow!!</h1>')
 
