from django.db import models


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
        return "Departamento {}, Direccion: {}".format(self.titulo,self.direccion)
    

class ImagenesDepartamento(models.Model):
    departamento = models.ForeignKey(Departamento,
                                     related_name="departamento_imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='departamentos/%Y/%m',blank=True)
    def __str__(self):
        return "Imagenes de deaprtamento {}".format(self.departamento)
    
