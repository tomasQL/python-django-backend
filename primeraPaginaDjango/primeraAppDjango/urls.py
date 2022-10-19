from django.urls import path
from . import views

urlpatterns = [
    path('fecha_actual/', views.mostrar_datetime),
]
