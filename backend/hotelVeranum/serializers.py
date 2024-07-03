from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario #, 'nombre'
        fields = ('idUsuario', 'usuario', 'correo', 'contrasena')
        extra_kwargs = {'contrasena': {'write_only': True}}

    def create(self, validated_data):
        validated_data['contrasena'] = make_password(validated_data.get('contrasena'))
        return super(UsuarioSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.contrasena = make_password(validated_data.get('contrasena', instance.contrasena))
        instance.save()
        return instance

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
        
class InventarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = HotelDetalle
        fields = '__all__'
        
class EventosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Customizar el token
        token['nombre'] = user.username
        token['contrasena'] = user.password
        return token
        