from rest_framework import viewsets
from .models import Vehiculo
from .serializers import VehiculoSerializer


# el ViewSet ya trae listar, ver, crear, editar y borrar
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
