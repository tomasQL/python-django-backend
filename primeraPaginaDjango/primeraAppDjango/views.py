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
    # OJO CON LOS STR CUANDO OPERAMOS, RECORDAR USAR +STR() para concatenar o usar en su defecto formateo por %s %()
    # resultados_operaciones="Resultado suma: ",sumar," Resultado resta: ",restar," Resultado multiplicación: ",multiplicar," Resultado división: ",dividir
    documento='''
    <!DOCTYPE html>
    <html>
        <body>
            <h2>Operaciónes con numeros (mediante la URI)</h2>
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

#  Func que permita ingresar un numero decimal y sumarle 1

def numeros_coma_flotante(request,valor_float):
    valor_ingresado_a_float=float(valor_float)
    n1=valor_ingresado_a_float+1.0
    n1=str(n1)
    respuesta="El resultado es: "+str(n1)
    return HttpResponse(respuesta)

#  Crear fun que permita ingresar nombre y 3 notas de un alumno 
#  Debe calcular e imprimir los datos ingresados
#  el promedio obtenido 
#  y la situación final del alumno 
#  si el promedio es mayor o igual a 4 aprueba o reprueba en caso contrario 
#  

#  Crear una func que permita ingresar dos numeros enteros
#  y calcule e imprima la tabla de multiplicar
#  del primer numero ingresado hasta el segundo numero ingresado
#  