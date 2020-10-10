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
   path('perfil/arriendos',views.perfil_arriendos,name="Mis arriendos"),
   path('admin/listar_usuarios/disponibilidad',views.listar_usuarios,name="Administracion usuarios"),
   path('admin/listar_usuarios/reserva',views.listar_usuarios,name="Administracion usuarios con reserva"),
   path('admin/listar_usuarios/arriendo',views.listar_usuarios,name="Administracion usuarios con arriendo"),
   path('admin/actualizar_estado_usuario/<int:id>/',views.actualizar_estado_usuario,name="Actualizar estado usuario"),
   path('admin/actualizar_llegada_usuario/<int:id>/',views.actualizar_llegada_usuario,name="Actualizar llegada usuario"),
   path('admin/generar_check_out/<int:id>/',views.generar_check_out,name="Generar check out"),
]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)