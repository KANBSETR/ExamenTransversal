from django.contrib import admin
from django.urls import path
from hotelVeranum import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('apix/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apix/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('region/', views.RegionList.as_view(), name='region-list'),
    path('region/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),
    
    #Habitaciones
    path('habitacion/', views.HabitacionList.as_view(), name='habitacion-list'),
    path('habitacion/<int:pk>/', views.HabitacionDetail.as_view(), name='habitacion-detail'),
    
    #Persona
    path('persona/', views.PersonaList.as_view(), name='persona-list'),
    path('persona/<int:pk>/', views.PersonaDetail.as_view(), name='persona-detail'),
    
    #Usuario 
    path('usuario/', views.UsuarioList.as_view(), name='usuario-list'),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario-detail'),
    
    #Empleado
    path('empleado/', views.EmpleadoList.as_view(), name='empleado-list'),
    path('empleado/<int:pk>/', views.EmpleadoDetail.as_view(), name='empleado-detail'),
    
    #TipoHabitacion
    path('tipoHabitacion/', views.TipoHabitacionList.as_view(), name='tipoHabitacion-list'),
    path('tipoHabitacion/<int:pk>/', views.TipoHabitacionDetail.as_view(), name='tipoHabitacion-detail'),
    
    #Servicio Adicional
    path('servicioAdicional/', views.ServicioAdicionalList.as_view(), name='servicioAdicional-list'),
    path('servicioAdicional/<int:pk>/', views.ServicioAdicionalDetail.as_view(), name='servicioAdicional-detail'),
    
    #Hotel
    path('hotel/', views.HotelList.as_view(), name='hotel-list'),
    path('hotel/<int:pk>/', views.HotelDetail.as_view(), name='hotel-detail'),
    
    #Reservas
    path('reserva/', views.ReservaList.as_view(), name='reserva-list'),
    path('reserva/<int:pk>/', views.ReservaDetail.as_view(), name='reserva-detail'),
    
    #Inventario
    path('inventario/', views.InventarioList.as_view(), name='inventario-list'),
    path('inventario/<int:pk>/', views.InventarioDetail.as_view(), name='inventario-detail'),
    
    #Eventos
    path('evento/', views.EventoList.as_view(), name='evento-list'),
    path('evento/<int:pk>/', views.EventoDetail.as_view(), name='evento-detail'),
    
]

