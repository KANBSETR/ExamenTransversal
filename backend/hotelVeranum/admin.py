from django.contrib import admin
from .models import *

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['idRegion','nombre']

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ['idProvincia','nombre','idRegion']

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list = ['idComuna','nombre','idProvincia']
    
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['idGenero','nombre','fCreacion']


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'comuna']

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['idCargo','nombreCargo']


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'idEmpleado', 'idCargo']
    

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['idUsuario', 'usuario']
    
    

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['idCategoria','nombre']
    
@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ['idTipoHabitacion','nombre','idCategoria']    
    
@admin.register(ServicioAdicional)
class ServicioAdicionalAdmin(admin.ModelAdmin):
    list_display = ['idServicioAdicional','nombre','precio']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['idHotel','patenteHotel','nombre','telefono','correo','direccion','estadoHabitacion','idComuna']

@admin.register(HotelDetalle)
class HotelDetalleAdmin(admin.ModelAdmin):
    list_display = ['idHotelDetalle','idHotel','idTipoHabitacion','idServicioAdicional']

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['idHabitacion','numeroHabitacion','cantDormitorios','cantBanos',
                    'cantCamas','tamanoCamas','cantPersonasDisp','descripcion','precio',
                    'estadoHabitacion','idServicioAdicional','idTipoHabitacion','idEmpleado','idHotel']


@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ['idFPago','nombre']

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ['idEvento','nombre','fechaInicio','fechaTermino','descripcion','precio','estado','idHotel','idFPago','idEmpleado','idUsuario']
    
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['idReserva','fechaInicio','fechaTermino','estado','idHabitacion','idUsuario']