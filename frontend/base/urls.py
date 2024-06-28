from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('registro/', views.registro, name='registro'),
    path('about/', views.about, name='about'),
    path('contraseñaOlvidada/', views.contraseñaOlvidada, name='contraseñaOlvidada'),
]
