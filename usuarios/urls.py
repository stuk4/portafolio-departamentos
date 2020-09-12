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
]
#Configuracion de imagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)