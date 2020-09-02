from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
# Urls de citt
urlpatterns = [
    path('',views.listar_departamentos,name="Departamentos"),
    path('departamento/<int:id>/',views.ver_departamento,name="Departamento"),
    path('departamentos/admin/',views.listar_departamentos_admin,name="Administracion departamentos"),
    path('departamentos/admin/eliminar_imagen/<int:id>/',views.eliminar_imagen_departamento,name="Eliminar imagen departamento"),

]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)