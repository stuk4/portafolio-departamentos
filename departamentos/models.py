from django.db import models
from django.utils.html import mark_safe


class Departamento(models.Model):

    titulo = models.CharField(null=True, blank=False, max_length=50)
    baños = models.PositiveIntegerField(null=True, blank=False)
    dormitorios = models.PositiveIntegerField(null=True, blank=False)
    descripcion = models.TextField(null=True)
    direccion = models.CharField(max_length=60)
    estado_mantencion = models.BooleanField(default=False,null=True, blank=True)
    mantencion = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)
    precio = models.PositiveIntegerField(null=True, blank=False)
    metros_cuadrados = models.PositiveIntegerField(null=True, blank=False)
    def __str__(self):
        return "ID {} Dep. {} Direc. {}".format(self.id,self.titulo,self.direccion)
    
  
class ImagenesDepartamento(models.Model):
    departamento = models.ForeignKey(Departamento,
                                     related_name="departamento_imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='departamentos/%Y/%m',blank=True)

    def mostrar_imagen(self):
        if self.imagen:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen))
        else:
            return mark_safe('<img src="/media/default.jpg" width="50" height="50" />')
    mostrar_imagen.short_description = 'imagen'
    def __str__(self):
        return "Imagen departamento {}".format(self.departamento)
    

  
