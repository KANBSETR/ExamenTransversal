from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import  Group, Permission
from django.utils.crypto import get_random_string
import uuid
from django.utils import timezone
from datetime import date



class Region (models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Provincia (models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.nombre + ', Region' + self.id_region.nombre

class Comuna (models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nombre + ', Provincia' + self.id_provincia.nombre

class Genero(models.Model):
    idGenero  = models.AutoField( primary_key=True,db_column='id_genero')
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
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    genero        = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')
    telefono = models.CharField(max_length=15)
    

    
    def __str__(self):
        return f'{self.nombre} {self.apPaterno} {self.apMaterno}'


class Cargo(models.Model): #steve
    idCargo = models.AutoField(null=False, primary_key=True, db_column='codCargo')
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
    codCargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    sueldo = models.IntegerField(null=False)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return f'Empleado: {self.rut.nombre} {self.rut.apPaterno}'    

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario=models.CharField(unique=True,max_length=20, null=False)
    nombre = models.CharField(max_length=50, blank=True, null=True) #Cuando el usuario quiera editar su perfil, agrega el nombre
    correo = models.EmailField(unique=True) 
    contrasena = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.usuario
    
#Ej: vip, nose ,normal ,etc
class Categoria (models.Model):
        id_categoria = models.AutoField(primary_key=True)
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
        id_tipo_habitacion = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        
        OPCIONES_TIPO_HABITACION = [
            ('Simple', 'Simple'),
            ('Doble', 'Doble'),
            ('Triple', 'Triple'),
            ('Matrimonial', 'Matrimonial'),
        ]
        
        tipos_habitaciones = models.CharField(max_length=50, choices=OPCIONES_TIPO_HABITACION, default='Simple')
        
        def __str__(self):
            return self.nombre

#Ej: wifi, tv, etc
class ServicioAdicional (models.Model):
        id_servicio = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        precio = models.IntegerField()
        
        
        def __str__(self):
            return self.nombre
    
class Hotel (models.Model):
        id_hotel = models.AutoField(primary_key=True)
        patente_hotel = models.CharField(max_length=50)
        nombre = models.CharField(max_length=50)
        telefono = models.CharField(max_length=50)
        correo = models.EmailField()
        direccion = models.CharField(max_length=50)
        estado_habitacion = models.BooleanField()      
        id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.nombre
        
class HotelDetalle (models.Model):
        id_hotel_detalle = models.AutoField(primary_key=True)
        descripcion = models.CharField(max_length=350)
        cantidad_habitaciones = models.IntegerField()
        cantidad_empleados = models.IntegerField()
        categoria_hotel = models.CharField(max_length=50)
        servicios_adicionales = models.CharField(max_length=50)
        id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
        id_tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
        id_servicio = models.ForeignKey(ServicioAdicional, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.id_hotel

class Habitacion (models.Model):
        id_habitacion = models.AutoField(primary_key=True)
        numero_habitacion = models.IntegerField()
        cant_banos = models.IntegerField()
        cant_camas = models.IntegerField()
        tamano_camas = models.CharField(max_length=50)
        cant_personas_disp = models.IntegerField()
        precio = models.IntegerField()
        estado_habitacion = models.CharField(max_length=50)
        servicios_adicionales = models.CharField(max_length=150)
        id_tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
        id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
        id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
        descripcion = models.CharField(max_length=50, null=True)
        
        def __str__(self):
            return self.descripcion
        
#Requerimiento 13 al 17 - Inventario 
class FormaPago(models.Model): 
    id_FPago = models.AutoField(null=False, primary_key=True,db_column='id_FPago')
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
    id_hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='id_hotel')
    id_FPago = models.ForeignKey(FormaPago, models.DO_NOTHING, db_column='id_FPago')
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    fModificacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    estado = models.BooleanField()
    id_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.idReserva


