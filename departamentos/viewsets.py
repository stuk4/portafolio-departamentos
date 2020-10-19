from rest_framework import viewsets
from rest_framework import serializers
from .models import Departamento
from .serializer import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.exclude(usuario__isnull=False).filter(estado_mantencion=True)
    serializer_class = DepartamentoSerializer