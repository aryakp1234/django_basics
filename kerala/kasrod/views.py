from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1><b><i>GODS OWN COUNTRY</i></b></h1>')
def about(request):
    return HttpResponse('<h2>about</h2><p>Kerala, a state on Indias tropical Malabar Coast, has nearly 600km of Arabian Sea shoreline.</p>')
def kasrod(request):
    return HttpResponse('<h2>kasaragod</h2><p>Kasaragod is a municipal town and administrative headquarters of Kasaragod district in the state of Kerala, India. </p>')