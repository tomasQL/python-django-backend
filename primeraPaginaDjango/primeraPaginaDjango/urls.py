"""primeraPaginaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from primeraAppDjango import views
from miNombre import views as viewsMiNombre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.display),
    #  path('fecha_actual/', views.mostrar_datetime), migrada a urls.py primeraAppDjango
    path('mi_nombre/', viewsMiNombre.mi_nombre),
    path('', include('primeraAppDjango.urls')),
    path('mostrar/<str:valor_datos>', views.capturar_dato),
    path('mostrar_numero/<int:valor_numerico>', views.capturar_numero),
]