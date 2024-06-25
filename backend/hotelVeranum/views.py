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