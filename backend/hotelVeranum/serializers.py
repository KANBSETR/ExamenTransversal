from rest_framework import serializers
from .models import *

class RegionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ProvinciaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class ComunaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class GeneroSerializer (serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        
class CargoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpleadoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TipoHabitacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'

class ServicioAdicionalSerializer (serializers.ModelSerializer):
    class Meta:
        model = ServicioAdicional
        fields = '__all__'

class HotelSerializer (serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HabitacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReservaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'