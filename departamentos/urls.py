from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
# Urls de citt
urlpatterns = [
    path('',views.listar_departamentos,name="Departamentos"),
    path('departamento/<int:id>/',views.ver_departamento,name="Departamento")

]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)