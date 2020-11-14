from .models import Departamento, Inventario
from rest_framework import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Departamento
        fields = ["id", "zona", "banos", "dormitorios", "direccion", "estado_mantencion", "precio", "metros_cuadrados"]

class InventarioSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    departamento_id = serializers.ReadOnlyField()
    class Meta:
        model = Inventario
        fields= ["id", "departamento_id", "nombre", "estado", "precio"]