from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from rest_framework import status

from hotelVeranum.models import Usuario  


from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def login(request):
    correo = request.data.get('correo')
    contrasena = request.data.get('contrasena')

    user = Usuario.objects.filter(correo=correo).first()

    if user is None:
        return Response({'error': 'Correo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    if not check_password(contrasena, user.contrasena):
        return Response({'error': 'Contraseña incorrecta.'}, status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
    
    
@api_view(['POST'])
def register(request):
    # Paso 1: Parsear los datos de la solicitud
    usuario = request.data.get('usuario')
    contrasena = request.data.get('contrasena')
    correo = request.data.get('correo')
    
    # Paso 2: Validar los datos (considera usar serializers para validación)
    if not usuario or not contrasena or not correo:
        return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Verificar si el usuario o el correo ya existen
    if Usuario.objects.filter(usuario=usuario).exists() or Usuario.objects.filter(correo=correo).exists():
        return Response({'error': 'El nombre de usuario o correo ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Paso 3: Crear un nuevo usuario
    Usuario.objects.create(
        usuario=usuario,
        correo=correo,
        contrasena=make_password(contrasena)  # Hashear la contraseña
    )
    
    # Paso 4: Devolver una respuesta
    return Response({'mensaje': 'Usuario registrado exitosamente.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def profile(request):
    return Response({''})