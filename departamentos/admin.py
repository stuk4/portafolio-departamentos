from django.contrib import admin
from .models import Departamento,ImagenesDepartamento,InventarioDepartamentos
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth import admin as auth_admin


from django.shortcuts import  redirect
from django.http import HttpResponseRedirect

from django.urls import reverse


admin.site.register(InventarioDepartamentos)
# Customizacion de modelo Departamento en admin
@admin.register(Departamento)
class CustomUserAdmin(admin.ModelAdmin):
    model = Departamento
    


    # Customizacion de interfaz
    list_display = ["mostrar_imagen","id","titulo","direccion",'mantencion','estado_mantencion']
    list_filter = ('titulo','direccion',)
    list_editable = ('estado_mantencion','mantencion')      

    # Metodo para asignar redireccion cuando se edita una imagen
    def response_change(self,request, obj):
        return redirect('Administracion departamentos')

# Customizacion de modelo ImagenesDepartamentos en admin
@admin.register(ImagenesDepartamento)
class CustomUserAdmin(admin.ModelAdmin):
    model = ImagenesDepartamento
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