from django.contrib import admin
from .models import Departamento,Imagen,Inventario,Reserva,Arriendo,Transporte,Tour,Check_in,Check_out
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth import admin as auth_admin


from django.shortcuts import  redirect
from django.http import HttpResponseRedirect

from django.urls import reverse


admin.site.register(Transporte)
admin.site.register(Inventario)
admin.site.register(Reserva)
admin.site.register(Arriendo)
admin.site.register(Tour)
admin.site.register(Check_in)
admin.site.register(Check_out)
# Customizacion de modelo Departamento en admin
@admin.register(Departamento)
class CustomUserAdmin(admin.ModelAdmin):
    model = Departamento
    

    exclude = ('estado_mantencion','mantencion','usuario',)
    # Customizacion de interfaz
    list_display = ["mostrar_imagen","id","titulo","direccion",'mantencion','estado_mantencion']
    list_filter = ('titulo','direccion',)
    list_editable = ('estado_mantencion','mantencion')      

    # Metodo para asignar redireccion cuando se edita una imagen
    def response_change(self,request, obj):
        return redirect('Administracion departamentos en mantención')
    def response_add(self,request,obj):
        return redirect('Administracion departamentos en mantención')

# Customizacion de modelo ImagenesDepartamentos en admin
@admin.register(Imagen)
class CustomUserAdmin(admin.ModelAdmin):
    model = Imagen
    list_display = ["mostrar_imagen",
                    "get_titulo", 
                    "get_direccion"
                    ]
    
    def get_titulo(self, obj):
        return obj.departamento.titulo
    get_titulo.short_description = "Deaprtamento"
    def get_direccion(self,obj):
        return obj.departamento.direccion
    get_direccion.short_description ="Direccion"

    list_filter = ('id',)
    # Metodo para asignar redireccion cuando se edita una imagen
    # def response_change(self,request, obj):
    #     return redirect('/')



#Edito los headers del admin
admin.site.site_header = "Administracion Departamentos"
admin.site.site_title = "Departamentos"
admin.site.index_title = 'Administracion'