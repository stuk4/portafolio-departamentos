from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe


class User(AbstractUser):
    rut = models.CharField(null=True,blank=False,max_length=13)
    telefono = models.IntegerField(null=True,blank=False)
    fecha_nacimiento = models.DateField( null=True,blank=False,auto_now=False, auto_now_add=False)
    N_tarjeta = models.IntegerField(null=True,blank=False)
    imagen = models.ImageField(upload_to='usuarios/%Y/%m',blank=True)
    
    #Metodo para mostrar imagen en admin
    def mostrar_imagen(self):
        if self.imagen:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen))
        else:
            return mark_safe('<img src="/media/default.jpg" width="50" height="50" />')

    mostrar_imagen.short_description = 'imagen'
    def __str__(self):
        return "{} {} Rut: {}".format(self.first_name,self.last_name,self.rut)


    class Meta:
        # Nombres del modelo en singular y plural
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
