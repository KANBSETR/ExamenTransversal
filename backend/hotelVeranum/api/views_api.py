from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from hotelVeranum.models import *
from hotelVeranum.api.serializers import *

class RegionViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer