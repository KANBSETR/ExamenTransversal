from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import  Group, Permission
from django.utils.crypto import get_random_string
import uuid
from django.utils import timezone
from datetime import date



class Region (models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Provincia (models.Model):
    idProvincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.nombre + ', Region' + self.idRegion.nombre

class Comuna (models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idProvincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nombre + ', Provincia' + self.idProvincia.nombre

class Genero(models.Model):
    idGenero  = models.AutoField( primary_key=True,db_column='idGenero')
    nombre     = models.CharField(max_length=20, blank=False, null=False,db_column='genero')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    # def __init__(self,id,codigo=None,genero=None):
    #     self.idGenero=id
    #     self.codigo=codigo
    #     self.genero=genero

    def __str__(self):
        return self.nombre
    
class Persona(models.Model):
    rut    = models.IntegerField(primary_key=True)
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apPaterno = models.CharField(max_length=30, blank=True, null=True)
    apMaterno = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=False)
    fechaNacimiento = models.DateField(blank=True, null=True,db_column='fecha_nacimiento')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idComuna')
    genero        = models.ForeignKey(Genero, models.DO_NOTHING, db_column='idGenero')
    telefono = models.CharField(max_length=15)
    

    
    def __str__(self):
        return f'{self.nombre} {self.apPaterno} {self.apMaterno}'


class Cargo(models.Model): #steve
    idCargo = models.AutoField(null=False, primary_key=True, db_column='idCargo')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    OPCIONES_CARGO = [
        ('Usuario', 'Usuario normal'),
        ('EncargadoHabitacion', 'Encargado de Habitaciones'),
        ('EncargadoInventario', 'Encargado de Inventario'),
        ('EncargadoServAdicional', 'Encargado de Servicios Adicionales'),
        ('EncargadoReserva', 'Encargado de Reservas'),
        ('EncargadoMantencion', 'Encargado de Mantención'),
        ('EncargadoFinanzas', 'Encargado de Finanzas'),
        ('EncargadoCliente', 'Encargado de Clientes'),
        ('EncargadoRestaurante', 'Encargado de Restaurante'),
        ('EncargadoBar', 'Encargado de Bar'),
        ('EncargadoSpa', 'Encargado de Spa'),
        ('EncargadoPiscina', 'Encargado de Piscina'),
        ('EncargadoGimnasio', 'Encargado de Gimnasio'),
        ('EncargadoSalonEventos', 'Encargado de Salón de Eventos'),
        ('EncargadoTienda', 'Encargado de Tienda'),
        ('EncargadoCocina', 'Encargado de Cocina'),
        ('EncargadoLavanderia', 'Encargado de Lavandería'),
        ('EncargadoRecepcion', 'Encargado de Recepción'),
        ('EncargadoSeguridad', 'Encargado de Seguridad'),
        ('EncargadoMascotas', 'Encargado de Mascotas'),
        ('EncargadoJardineria', 'Encargado de Jardinería'),
        ('EncargadoAseo', 'Encargado de Aseo'),
        ('EncargadoMensajeria', 'Encargado de Mensajería'),
        ('EncargadoEstacionamiento', 'Encargado de Estacionamiento'),
        ('EncargadoMantVehiculos', 'Encargado de Mantención de Vehículos'),
        ('EncargadoMantMaquinaria', 'Encargado de Mantención de Maquinaria'),
        ('EncargadoMantEquipos', 'Encargado de Mantención de Equipos'),
        ('EncargadoMantInfraestructura', 'Encargado de Mantención de Infraestructura'),
        ('EncargadoMantTecnologia', 'Encargado de Mantención de Tecnología'),
        ('EncargadoMantRedes', 'Encargado de Mantención de Redes'),
        ('EncargadoMantSistemas', 'Encargado de Mantención de')
    ]
    nombreCargo = models.CharField(max_length=100)

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)  
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    usuario = models.CharField(max_length=20, null=False)
    clave = models.CharField(max_length=10, null=False)
    idCargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    sueldo = models.IntegerField(null=False)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return f'Empleado: {self.rut.nombre} {self.rut.apPaterno}'    

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    usuario=models.CharField(unique=True,max_length=20, null=False)
    nombre = models.CharField(max_length=50, blank=True, null=True) #Cuando el usuario quiera editar su perfil, agrega el nombre
    correo = models.EmailField(unique=True) 
    contrasena = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.usuario
    
#Ej: vip, nose ,normal ,etc
class Categoria (models.Model):
        idCategoria = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        
        OPCIONES_CATEGORIA = [
            ('Vip', 'Vip'),
            ('Normal', 'Normal'),
            ('Economico', 'Economico'),
            ('Familiar', 'Familiar'),
            ('Suite', 'Suite'),
            ('Presidencial', 'Presidencial')
        ]
        
        categorias = models.CharField(max_length=50, choices=OPCIONES_CATEGORIA, default='Normal')
        
        def __str__(self):
            return self.nombre
        
#Ej: habitacion simple, doble, triple, etc
class TipoHabitacion (models.Model):
        idTipoHabitacion = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        
        OPCIONES_TIPO_HABITACION = [
            ('Simple', 'Simple'),
            ('Doble', 'Doble'),
            ('Triple', 'Triple'),
            ('Matrimonial', 'Matrimonial'),
        ]
        
        tiposHabitaciones = models.CharField(max_length=50, choices=OPCIONES_TIPO_HABITACION, default='Simple')
        
        def __str__(self):
            return self.nombre

#Ej: wifi, tv, etc
class ServicioAdicional (models.Model):
        idServicioAdicional = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        precio = models.IntegerField()
        
        
        def __str__(self):
            return self.nombre
    
class Hotel (models.Model):
        idHotel = models.AutoField(primary_key=True)
        patenteHotel = models.CharField(max_length=50)
        nombre = models.CharField(max_length=50)
        telefono = models.CharField(max_length=50)
        correo = models.EmailField()
        direccion = models.CharField(max_length=50)
        estadoHabitacion = models.BooleanField()      
        idComuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.nombre
        
class HotelDetalle (models.Model):
        idHotelDetalle = models.AutoField(primary_key=True)
        descripcion = models.CharField(max_length=350)
        cantidadHabitaciones = models.IntegerField()
        cantidadEmpleados = models.IntegerField()
        categoriaHotel = models.CharField(max_length=50)
        idServicioAdicional = models.ForeignKey(ServicioAdicional, on_delete=models.CASCADE)
        idHotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
        idTipoHabitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
        idServicioAdicional = models.ForeignKey(ServicioAdicional, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.descripcion

class Habitacion (models.Model):
        idHabitacion = models.AutoField(primary_key=True)
        numeroHabitacion = models.IntegerField()
        cantDormitorios = models.IntegerField()
        cantBanos = models.IntegerField()
        cantCamas = models.IntegerField()
        tamanoCamas = models.CharField(max_length=50)
        cantPersonasDisp = models.IntegerField()
        precio = models.IntegerField()
        estadoHabitacion = models.CharField(max_length=50)
        idServicioAdicional = models.ForeignKey(ServicioAdicional, on_delete=models.CASCADE)
        idTipoHabitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
        idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
        idHotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
        descripcion = models.CharField(max_length=50, null=True)
        
        def __str__(self):
            return self.descripcion
        
#Requerimiento 13 al 17 - Inventario 
class FormaPago(models.Model): 
    idFPago = models.AutoField(null=False, primary_key=True,db_column='idFPago')
    nombre = models.CharField(max_length=200, null=False,db_column='nombre')
    
    def __str__(self):
        return self.nombre

class Eventos(models.Model):
    idEvento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    estado = models.BooleanField()
    idHotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='idHotel')
    idFPago = models.ForeignKey(FormaPago, models.DO_NOTHING, db_column='idFPago')
    idEmpleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idEmpleado')
    idUsuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idUsuario')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    fModificacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    precioReserva = models.IntegerField()
    estado = models.BooleanField()
    idHabitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.idUsuario.usuario + ' ' + self.idHabitacion.descripcion


