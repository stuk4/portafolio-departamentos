from .models import Departamento
# from .models import Inventario
# from .models import Reserva
# from .models import Transporte
# from .models import Tour
# from .models import Check_in
# from .models import Check_out
from rest_framework import serializers

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["zona", "banos", "dormitorios", "direccion", "estado_mantencion", "precio", "metros_cuadrados"]


## APIS PARA LUEGO EN CASO DE NECESITARLAS, SI NO, BORRAR COMENTARIOS

# class InventarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Inventario
#         fields = ["estados", "departamento", "nombre", "estado", "precio"]

# class ReservaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reserva
#         fields = ["usuario", "departamento", "acompanantes", "llegada", "dia_llegada", "abono", "dias_estadia"]

# class TransporteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transporte
#         fields = ["reserva", "fecha_solicitud", "estado_verificado", "precio", "desde", "hacia", "hora", "vehiculo", "conductor"]

# class TourSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tour
#         fields = ["departamento", "reserva", "nombre", "dia", "duracion", "direccion", "precio", "descripcion"]

# class Check_inSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Check_in
#         fields = ["arriendo", "diferencia", "total"]

# class Check_outSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Check_out
#         fields = ["estados", "arriendo", "estado", "valor_danos", "valor_transporte", "valor_tours", "total"]

