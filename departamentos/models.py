from django.db import models
from django.utils.html import mark_safe
from datetime import date,timedelta

class Departamento(models.Model):

    mantencion = models.DateField(
        null=True, blank=True,default=date.today, auto_now=False, auto_now_add=False)
    titulo = models.CharField(null=True, blank=False, max_length=50)
    usuario = models.OneToOneField("usuarios.User", related_name="usuario",blank=True,null=True, on_delete=models.CASCADE)
    banos = models.PositiveIntegerField(null=True, blank=False,verbose_name="baños")
    dormitorios = models.PositiveIntegerField(null=True, blank=False)
    descripcion = models.TextField(null=True)
    direccion = models.CharField(max_length=60)
    estado_mantencion = models.BooleanField(default=True,null=True, blank=True)
    imagen = models.ImageField(upload_to='departamentos_principal/%Y/%m',blank=True)
    precio = models.PositiveIntegerField(null=True, blank=False)
    metros_cuadrados = models.PositiveIntegerField(null=True, blank=False)
    @property
    def dia_mantencion(self):
        return date.today() == self.mantencion
   
    def __str__(self):
        return "ID {} Dep. {} Direc. {}".format(self.id,self.titulo,self.direccion)
    def mostrar_imagen(self):
        if self.imagen:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen))
        else:
            return mark_safe('<img src="/media/default.jpg" width="50" height="50" />')
    mostrar_imagen.short_description = 'imagen'
  
    

class Imagen(models.Model):
    departamento = models.ForeignKey(Departamento,
                                     related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='departamentos/%Y/%m',blank=False,null=True)
    

    def mostrar_imagen(self):
        if self.imagen:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen))
        else:
            return mark_safe('<img src="/media/default.jpg" width="50" height="50" />')
    mostrar_imagen.short_description = 'imagen'
    def __str__(self):
        return "Imagen departamento {}".format(self.departamento)

class Inventario(models.Model):
    estados = (('Buen estado','Buen estado'),
            ('Mal estado','Mal estado'))
    departamento = models.ForeignKey(Departamento,
                                     related_name="inventario", on_delete=models.CASCADE)
    nombre = models.CharField(null=False,blank=False,max_length=50)
    estado =models.CharField(max_length=20,choices=estados,default='Buen estado',null=True,blank=False)
    precio = models.PositiveIntegerField(null=False, blank=False)
    
    def __str__(self):
        return 'Nombre: {} Estado:{}'.format(self.nombre,self.estado)

class Reserva(models.Model):
    usuario = models.ForeignKey("usuarios.User",null=True,blank=True ,related_name="reserva", on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, related_name="reserva", on_delete=models.CASCADE)
    acompanantes = models.PositiveIntegerField(null=True,blank=True,verbose_name="acompañantes" )
    dia_llegada = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)
    abono = models.PositiveIntegerField(null=False,blank=False )
    dias_estadia =  models.PositiveIntegerField(null=False,blank=False,verbose_name="días estadia" )

    @property
    def dia_salida(self):
        return self.dia_llegada + timedelta(days=self.dias_estadia)

    @property
    def diferencia(self):
        return (self.departamento.precio * self.dias_estadia) - self.abono
    @property
    def total(self):
        return self.departamento.precio * self.dias_estadia
    def __str__(self):
        return 'ID reserva:{} {}'.format(self.id,self.usuario)
class Transporte(models.Model):
    reserva = models.OneToOneField(Reserva, related_name="transporte", on_delete=models.CASCADE)
    estado_verificado = models.BooleanField(default=False)
    desde = models.CharField(null=False,blank=False,max_length=50)
    hacia =  models.CharField(null=False,blank=False,max_length=50)
    hora = models.TimeField(blank=True,null=True,auto_now=False, auto_now_add=False)
    vehiculo = models.CharField(null=True,blank=True,max_length=50)
    conductor = models.CharField(null=True,blank=True,max_length=50)

class Arriendo(models.Model):
    reserva = models.ForeignKey(Reserva, related_name="arriendo", on_delete=models.CASCADE)
    diferencia = models.PositiveIntegerField(null=True,blank=True )
    total = models.PositiveIntegerField(null=False,blank=False )
    def __str__(self):
        return '{}'.format(self.reserva)



