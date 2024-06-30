from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

#JsonResponse de confirmacion
class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)


class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)

#Definicio de las vistas Habitacion
def habitacion(request):
    registro = Habitacion.objects.all()
    print("Registro", registro)
    serializer = HabitacionSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class HabitacionList(APIView):
    def get(self, request, format=None):
        habitaciones = Habitacion.objects.all()
        serializer = HabitacionSerializer(habitaciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HabitacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitacionDetail(APIView):
    def get_object(self, pk):
        try:
            return Habitacion.objects.get(pk=pk)
        except Habitacion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        habitacion = self.get_object(pk)
        serializer = HabitacionSerializer(habitacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        habitacion = self.get_object(pk)
        serializer = HabitacionSerializer(habitacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        habitacion = self.get_object(pk)
        habitacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def api_root(request):
    return JsonResponse({
        'message': 'Bienvenido a la API del Hotel Veranum',
        'routes': {
            'habitaciones': '/api/habitacion/',
        }
    })
    
    
#Reserva
def reserva(request):
    registro = Reserva.objects.all()
    print("Registro", registro)
    serializer = ReservaSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ReservaList(APIView):
    def get(self, request, format=None):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegionViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReservaDetail(APIView):
    def get_object(self, pk):
        try:
            return Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reserva = self.get_object(pk)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Persona

def persona(request):
    registro = Persona.objects.all()
    print("Registro", registro)
    serializer = PersonaSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class PersonaList(APIView):
    def get(self, request, format=None):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonaDetail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Usuario UsuarioSerializer 

def usuario(request):
    registro = Usuario.objects.all()
    print("Registro", registro)
    serializer = UsuarioSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class UsuarioList(APIView):
    def get(self, request, format=None):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetail(APIView):
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Empleado EmpleadoSerializer

def empleado(request):
    registro = Empleado.objects.all()
    print("Registro", registro)
    serializer = EmpleadoSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class EmpleadoList(APIView):
    def get(self, request, format=None):
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadoDetail(APIView):
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# TipoHabitacion TipoHabitacionSerializer

def tipoHabitacion(request):
    registro = TipoHabitacion.objects.all()
    print("Registro", registro)
    serializer = TipoHabitacionSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class TipoHabitacionList(APIView):
    def get(self, request, format=None):
        tipoHabitaciones = TipoHabitacion.objects.all()
        serializer = TipoHabitacionSerializer(tipoHabitaciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoHabitacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoHabitacionDetail(APIView):
    def get_object(self, pk):
        try:
            return TipoHabitacion.objects.get(pk=pk)
        except TipoHabitacion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tipoHabitacion = self.get_object(pk)
        serializer = TipoHabitacionSerializer(tipoHabitacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tipoHabitacion = self.get_object(pk)
        serializer = TipoHabitacionSerializer(tipoHabitacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ServicioAdicional ServicioAdicionalSerializer
def servicioAdicional(request):
    registro = ServicioAdicional.objects.all()
    print("Registro", registro)
    serializer = ServicioAdicionalSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ServicioAdicionalList(APIView):
    def get(self, request, format=None):
        servicioAdicionales = ServicioAdicional.objects.all()
        serializer = ServicioAdicionalSerializer(servicioAdicionales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicioAdicionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicioAdicionalDetail(APIView):
    def get_object(self, pk):
        try:
            return ServicioAdicional.objects.get(pk=pk)
        except ServicioAdicional.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        servicioAdicional = self.get_object(pk)
        serializer = ServicioAdicionalSerializer(servicioAdicional)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        servicioAdicional = self.get_object(pk)
        serializer = ServicioAdicionalSerializer(servicioAdicional, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Hotel HotelSerializer

def hotel(request):
    registro = Hotel.objects.all()
    print("Registro", registro)
    serializer = HotelSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class HotelList(APIView):
    def get(self, request, format=None):
        hoteles = Hotel.objects.all()
        serializer = HotelSerializer(hoteles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelDetail(APIView):
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Eventos EventosSerializer
def eventos(request):
    registro = Eventos.objects.all()
    print("Registro", registro)
    serializer = EventosSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class EventosList(APIView):
    def get(self, request, format=None):
        eventos = Eventos.objects.all()
        serializer = EventosSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventosDetail(APIView):
    def get_object(self, pk):
        try:
            return Eventos.objects.get(pk=pk)
        except Eventos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        eventos = self.get_object(pk)
        serializer = EventosSerializer(eventos)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        eventos = self.get_object(pk)
        serializer = EventosSerializer(eventos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        eventos = self.get_object(pk)
        eventos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ServicioAdicional ServicioAdicionalSerializer
def servicioAdicional(request):
    registro = ServicioAdicional.objects.all()
    print("Registro", registro)
    serializer = ServicioAdicionalSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ServicioAdicionalList(APIView):
    def get(self, request, format=None):
        servicio = ServicioAdicional.objects.all()
        serializer = ServicioAdicionalSerializer(servicio, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicioAdicionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ServicioAdicionalDetail(APIView):
    def get_object(self, pk):
        try:
            return ServicioAdicional.objects.get(pk=pk)
        except ServicioAdicional.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        servicio = self.get_object(pk)
        serializer = ServicioAdicionalSerializer(servicio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        servicio = self.get_object(pk)
        serializer = ServicioAdicionalSerializer(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        servicio = self.get_object(pk)
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Inventario InventarioSerializer

def inventario(request):
    registro = HotelDetalle.objects.all()
    print("Registro", registro)
    serializer = InventarioSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class InventarioList(APIView):
    def get(self, request, format=None):
        inventarios = HotelDetalle.objects.all()
        serializer = InventarioSerializer(inventarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InventarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InventarioDetail(APIView):
    def get_object(self, pk):
        try:
            return HotelDetalle.objects.get(pk=pk)
        except HotelDetalle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventario = self.get_object(pk)
        serializer = InventarioSerializer(inventario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        inventario = self.get_object(pk)
        serializer = InventarioSerializer(inventario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        inventario = self.get_object(pk)
        inventario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    
