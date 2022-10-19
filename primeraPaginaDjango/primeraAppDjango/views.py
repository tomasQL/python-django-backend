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
    #  Manejo DIVISIÓN POR 0 => Indeterminado
    if numero2==0:
        dividir="División por 0 indeterminada"    
    else:
        dividir=numero1/numero2
    # resultados_operaciones="Resultado suma: ",sumar," Resultado resta: ",restar," Resultado multiplicación: ",multiplicar," Resultado división: ",dividir
    documento='''
    <!DOCTYPE html>
    <html>
        <body>
            <h2>Operaciónes con numeros (mediante la url)</h2>
            <h3>Suma, resta, multiplicación y división</h3>
            <ol>
              <li>EL resultado de la suma es: %s</li>
              <li>EL resultado de la resta es: %s</li>
              <li>EL resultado de la multiplicación es: %s</li>
              <li>EL resultado de la división es: %s</li>
            </ol> 
        </body>
    </html>
    '''%(sumar,restar,multiplicar,dividir)
    return HttpResponse(documento)