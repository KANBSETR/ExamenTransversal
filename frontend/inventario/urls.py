from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.inventario, name='inventario'),
]
