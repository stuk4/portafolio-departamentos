from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth import admin as auth_admin


from django.shortcuts import  redirect



@admin.register(User)
class CustomUserAdmin(UserAdmin):
   list_display = ["mostrar_imagen",
                    "username", 
                    "is_superuser"]
   fieldsets = (("User", {"fields": ("telefono","edad","reserva_activa",'arriendo_activo',"N_tarjeta","imagen",)}),) + auth_admin.UserAdmin.fieldsets
   exclude = ('usuario',)
   def response_add(self,request,obj):
      return redirect('Administracion usuarios')
   def response_change(self,request, obj):
      return redirect('Administracion usuarios')


