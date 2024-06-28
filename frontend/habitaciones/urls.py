from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.habitacion, name='habitacion'),
]
