from .models import Departamento
from rest_framework import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Departamento
        fields = ["id", "zona", "banos", "dormitorios", "direccion", "estado_mantencion", "precio", "metros_cuadrados"]