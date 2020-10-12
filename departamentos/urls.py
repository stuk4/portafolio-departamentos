from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework import routers
from .viewsets import DepartamentoViewSet
from usuarios.viewsets import UserViewSet

## APIS PARA LUEGO EN CASO DE NECESITARLAS, SI NO, BORRAR COMENTARIOS

# from .viewsets import InventarioViewSet
# from .viewsets import ReservaViewSet
# from .viewsets import TransporteViewSet
# from .viewsets import TourViewSet
# from .viewsets import Check_inViewSet
# from .viewsets import Check_outViewSet

router = routers.SimpleRouter()
router.register('departamentos', DepartamentoViewSet)
router.register('usuarios', UserViewSet)
# router.register('inventario', InventarioViewSet)
# router.register('reserva', ReservaViewSet)
# router.register('transporte', TransporteViewSet)
# router.register('tour', TourViewSet)
# router.register('check_in', Check_inViewSet)
# router.register('check_out', Check_outViewSet)

from . import views
# Urls de citt  
urlpatterns = [
    path('',views.listar_departamentos,name="Departamentos"),
    path('departamento/<int:id>/',views.ver_departamento,name="Departamento"),
    path('departamentos/admin/',views.listar_departamentos_admin,name="Administracion departamentos"),
    path('departamentos_mantencion/admin/',views.listar_departamentos_admin,name="Administracion departamentos en mantención"),
    path('departamentos_reservados/admin/',views.listar_departamentos_admin,name="Administracion departamentos reservados"),
    path('departamentos_arrendados/admin/',views.listar_departamentos_admin,name="Administracion departamentos arrendados"),
    path('departamentos/admin/eliminar_imagen/<int:id>/',views.eliminar_imagen_departamento,name="Eliminar imagen departamento"),
    path('departamentos/admin/eliminar_inventario/<int:id>/',views.eliminar_inventario_departamento,name="Eliminar inventario departamento"),
    path('departamentos/admin/eliminar_tour/<int:id>/',views.eliminar_tour_departamento,name="Eliminar tour departamento"),
    path('departamentos/admin/eliminar_departamento/<int:id>/',views.eliminar_departamento,name="Eliminar departamento"),
    path('departamentos/admin/actualizar_estado_mantencion/<int:id>/',views.actualizar_estado_mantencion,name="Actualizar estado mantencion"),
    path('departamentos/admin/actualizar_estado_inventario/<int:id>/',views.actualizar_estado_inventario,name="Actualizar inventario departamento"),
    #Sección apis
    path('api/',include(router.urls)),
]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)