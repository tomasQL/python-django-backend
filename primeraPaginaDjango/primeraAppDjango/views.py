from __future__ import division
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
    #  Esta no es la forma, normalmente usaremos templates, pero tamos practicando
    documento = '''
    <html>
        <body>
            <h1>El valor ingresado es %s </h1>
        </body>
    </html>
    '''
    return HttpResponse(documento)

def capturar_numero(request,valor_numerico):
    valor_numerico+=1
    return HttpResponse(valor_numerico)

# crear func que permita ingresar 2 numeros, calcular suma resta mult div

def operar_numeros(request,numero1,numero2):
    sumar=numero1+numero2
    restar=numero1-numero2
    multiplicar=numero1*numero2
    dividir=numero1/numero2
    resultados_operaciones="Resultado suma: ",sumar," Resultado resta: ",restar," Resultado multiplicación: ",multiplicar," Resultado división: ",dividir
    return HttpResponse(resultados_operaciones)