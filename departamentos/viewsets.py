from rest_framework import viewsets
from rest_framework import serializers

from .models import Departamento

## APIS PARA LUEGO EN CASO DE NECESITARLAS, SI NO, BORRAR COMENTARIOS

# from .models import Inventario
# from .models import Reserva
# from .models import Transporte
# from .models import Tour
# from .models import Check_in
# from .models import Check_out
from .serializer import DepartamentoSerializer
# from .serializer import InventarioSerializer
# from .serializer import ReservaSerializer
# from .serializer import TransporteSerializer
# from .serializer import TourSerializer
# from .serializer import Check_inSerializer
# from .serializer import Check_outSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.exclude(usuario__isnull=False).filter(estado_mantencion=True)
    serializer_class = DepartamentoSerializer

# class InventarioViewSet(viewsets.ModelViewSet):
#     queryset = Inventario.objects.all()
#     serializer_class = InventarioSerializer

# class ReservaViewSet(viewsets.ModelViewSet):
#     queryset = Reserva.objects.all()
#     serializer_class = ReservaSerializer

# class TransporteViewSet(viewsets.ModelViewSet):
#     queryset = Transporte.objects.all()
#     serializer_class = TransporteSerializer

# class TourViewSet(viewsets.ModelViewSet):
#     queryset = Tour.objects.all()
#     serializer_class = TourSerializer

# class Check_inViewSet(viewsets.ModelViewSet):
#     queryset = Check_in.objects.all()
#     serializer_class = Check_inSerializer

# class Check_outViewSet(viewsets.ModelViewSet):
#     queryset = Check_out.objects.all()
#     serializer_class = Check_outSerializer