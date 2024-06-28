from rest_framework.decorators import api_view
from rest_framework.response import Response
from hotelVeranum.models import Usuario  

from django.contrib.auth.hashers import make_password
from rest_framework import status

@api_view(['POST'])
def login(request):
    return Response({''})
    
    
    
@api_view(['POST'])
def register(request):
    # Paso 1: Parsear los datos de la solicitud
    usuario = request.data.get('usuario')
    contrasena = request.data.get('contrasena')
    email = request.data.get('email')
    
    # Paso 2: Validar los datos (considera usar serializers para validación)
    if not usuario or not contrasena or not email:
        return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Verificar si el usuario o el correo ya existen
    if Usuario.objects.filter(usuario=usuario).exists() or Usuario.objects.filter(correo=email).exists():
        return Response({'error': 'El nombre de usuario o correo ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Paso 3: Crear un nuevo usuario
    Usuario.objects.create(
        usuario=usuario,
        correo=email,
        contrasena=make_password(contrasena)  # Hashear la contraseña
    )
    
    # Paso 4: Devolver una respuesta
    return Response({'mensaje': 'Usuario registrado exitosamente.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def profile(request):
    return Response({''})