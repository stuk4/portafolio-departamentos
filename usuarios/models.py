from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    rut = models.CharField(null=True,blank=False,max_length=13)
    telefono = models.IntegerField(null=True,blank=False)
    fecha_nacimiento = models.DateField( null=True,blank=False,auto_now=False, auto_now_add=False)
    N_tarjeta = models.IntegerField(null=True,blank=False)
    imagen = models.ImageField(upload_to='usuarios/%Y/%m',blank=True)
    
    def __str__(self):
        return "{} {} Rut: {}".format(self.first_name,self.last_name,self.rut)
    

    class Meta:
        # Nombres del modelo en singular y plural
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
