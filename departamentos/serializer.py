from .models import Departamento
from rest_framework import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["titulo", "banos", "dormitorios", "descripcion", "direccion", "estado_mantencion", "precio", "metros_cuadrados"]