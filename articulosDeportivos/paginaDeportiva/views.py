from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.


def index(request):
    
    return render(request, "index.html",)

def productos(request):
    
    return render(request, "productos.html", )

def acercade(request):
    
    return render(request, "acercade.html", )