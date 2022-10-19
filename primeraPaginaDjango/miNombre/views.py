from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mi_nombre(request):
    return HttpResponse("<p>Mi nombre es Tomás Gatica<p>")