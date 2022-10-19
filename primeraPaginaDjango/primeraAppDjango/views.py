from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def display(request):
    return HttpResponse("<h1>Primer request de prueba, esto devuelve un h1</h1>")

def mostrar_datetime(request):
    dt = datetime.datetime.now()
    #  La funcion datetime nos devolvera un elemento en formato UTC por lo que no
    #  sera la misma zona horaria
    s = "<b>La fecha actual es: </b>"+str(dt)
    return HttpResponse(s)

def capturar_dato(request,valor_datos):
    x = "usted digitó %s"%valor_datos
    documento = '''<html> '''
    return HttpResponse(x)