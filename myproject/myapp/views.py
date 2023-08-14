from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myText(request):
    return HttpResponse("<h3>Hello World</h3>")