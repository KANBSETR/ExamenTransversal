from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserva, name='reserva'),
    path('completarReserva/', views.completar_reserva, name='completar_reserva'),
    path('pagoCompletado/', views.pago, name='pago'),
]
