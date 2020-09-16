from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from datetime import date
from departamentos.models import Transporte
class User(AbstractUser):
    telefono = models.IntegerField(null=True,blank=False)
    fecha_nacimiento = models.DateField( null=True,blank=False,auto_now=False, auto_now_add=False)
    N_tarjeta = models.IntegerField(null=True,blank=False)
    imagen = models.ImageField(upload_to='usuarios/%Y/%m',blank=True)
    
    # Metodo para obtener el transporte  actual del usuario
  
    def transporte(self):   
        reserva  =self.reserva.filter(usuario=self.id).last()
        transporte = Transporte.objects.get(reserva=reserva.id) 
        return transporte
        #Metodo para mostrar imagen en admin
    def mostrar_imagen(self):
        if self.imagen:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen))
        else:
            return mark_safe('<img src="/media/default.jpg" width="50" height="50" />')
    mostrar_imagen.short_description = 'imagen'
    
    def __str__(self):
        return "{} {} ".format(self.first_name,self.last_name)


    class Meta:
        # Nombres del modelo en singular y plural
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
