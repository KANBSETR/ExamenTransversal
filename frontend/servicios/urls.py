from django.urls import path
from . import views

urlpatterns = [
    path('servicio/', views.servicios, name='servicios'),
    path('servicio/actualizar/', views.modificar_servicio, name='modificar_servicio'),
]
