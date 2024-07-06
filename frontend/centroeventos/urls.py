from django.urls import path
from . import views

urlpatterns = [
    path('evento/', views.eventos, name='eventos'),
    path('evento/actualizar/', views.evento_modificar, name='evento_modificar')
    
]
