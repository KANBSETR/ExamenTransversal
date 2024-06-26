from django.contrib import admin
from django.urls import path
from hotelVeranum import views


urlpatterns = [
    #Habitaciones
    path('habitacion/', views.HabitacionList.as_view(), name='habitacion-list'),
    path('habitacion/<int:pk>/', views.HabitacionDetail.as_view(), name='habitacion-detail'),
    
    #Reservas
    path('reserva/', views.ReservaList.as_view(), name='reserva-list'),
    path('reserva/<int:pk>/', views.ReservaDetail.as_view(), name='reserva-detail'),
    
    path('', views.api_root, name='api_root'),
]

