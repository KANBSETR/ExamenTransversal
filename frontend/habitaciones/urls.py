from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.habitacion, name='habitacion'),
    path('habitaciones/actualizar/', views.modificar_habitacion, name='modificar_habitacion')
]
