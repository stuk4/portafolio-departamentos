from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# Urls de usuarios /usuarios/
urlpatterns = [
   path('login/',views.login_view,name="login"),
   path('logout/',views.logout_view,name="logout"),
   path('registro/',views.registro,name="registro"),
   path('perfil/',views.perfil,name="Perfil"),
   path('perfil/reservas',views.perfil_reservas,name="Mis reservas"),
   path('admin/listar_usuarios/disponibilidad',views.listar_usuarios,name="Administracion usuarios"),
   path('admin/listar_usuarios/reserva',views.listar_usuarios,name="Administracion usuarios con reserva"),
   path('admin/actualizar_estado_usuario/<int:id>/',views.actualizar_estado_usuario,name="Actualizar estado usuario"),
]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)