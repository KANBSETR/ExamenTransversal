from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('registro/', views.registro, name='registro'),
    path('about/', views.about, name='about'),
    path('contraseñaOlvidada/', views.contraseñaOlvidada, name='contraseñaOlvidada'),
    
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/actualizarUsuarios/', views.actualizarUsuarios, name='actualizarUsuarios'),
    
    path('empleados/', views.empleados, name='empleados'),
    path('empleados/actualizarEmpleados/', views.actualizarEmpleados, name='actualizarEmpleados'),
]
