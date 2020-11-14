from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import generics
from .models import Departamento, Inventario
from .serializer import DepartamentoSerializer, InventarioSerializer

class DepartamentoMantencionViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.exclude(usuario__isnull=False).filter(estado_mantencion=True)
    serializer_class = DepartamentoSerializer

class DepartamentosDisponiblesViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.exclude(usuario__isnull=False).filter(estado_mantencion=False)
    serializer_class = DepartamentoSerializer

class InventarioViewset(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer