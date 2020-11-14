from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework import routers
from .viewsets import DepartamentoMantencionViewSet, DepartamentosDisponiblesViewSet, InventarioViewset
from usuarios.viewsets import UserViewSet
from . import views

router = routers.SimpleRouter()
router.register('departamentos_mantencion', DepartamentoMantencionViewSet)
router.register('departamentos_disponibles', DepartamentosDisponiblesViewSet)
router.register('inventario', InventarioViewset)
#router.register(r'inventario/(?P<departamento_id>/d+)', InventarioViewset)
router.register('usuarios', UserViewSet)

# Urls de citt  
urlpatterns = [
    path('',views.listar_departamentos,name="Departamentos"),
    path('departamento/<int:id>/',views.ver_departamento,name="Departamento"),
    # Seccion listar departamentos   
    path('departamentos/admin/',views.listar_departamentos_admin,name="Administracion departamentos"),
    path('departamentos_mantencion/admin/',views.listar_departamentos_admin,name="Administracion departamentos en mantención"),
    path('departamentos_reservados/admin/',views.listar_departamentos_admin,name="Administracion departamentos reservados"),
    path('departamentos_arrendados/admin/',views.listar_departamentos_admin,name="Administracion departamentos arrendados"),
    # Seccion eliminar 
    path('departamentos/admin/eliminar_imagen/<int:id>/',views.eliminar_imagen_departamento,name="Eliminar imagen departamento"),
    path('departamentos/admin/eliminar_inventario/<int:id>/',views.eliminar_inventario_departamento,name="Eliminar inventario departamento"),
    path('departamentos/admin/eliminar_tour/<int:id>/',views.eliminar_tour_departamento,name="Eliminar tour departamento"),
    path('departamentos/admin/eliminar_departamento/<int:id>/',views.eliminar_departamento,name="Eliminar departamento"),
    # Seccion mantencion
    path('departamentos/admin/actualizar_estado_mantencion/<int:id>/',views.actualizar_estado_mantencion,name="Actualizar estado mantencion"),
    path('departamentos/admin/actualizar_estado_inventario/<int:id>/',views.actualizar_estado_inventario,name="Actualizar inventario departamento"),
    # Seccion reportes
    path('departamentos/admin/reportes_reserva/',views.reportes_departamentos,name="Reportes departamento reservas"),
    path('departamentos/admin/reportes_arriendo/',views.reportes_departamentos,name="Reportes departamento arriendos"),
    path('departamentos/admin/reportes_reserva/generar/<int:id>/',views.generar_informe_reserva,name="Generar reporte reserva"),
    path('departamentos/admin/reportes_arriendo/generar/<int:id>/',views.generar_informe_arriendo,name="Generar reporte arriendo"),
    #Sección apis
    path('api/',include(router.urls)),
]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)