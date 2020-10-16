from django.db import models
from django.utils.html import mark_safe
from datetime import date,timedelta
from django.contrib.auth.models import User 
class Departamento(models.Model):
    zonas = (('Sur','Sur'),
        ('Este','Este'),
        ('Oeste','Oeste'),
        ('Norte','Norte'))
        
    mantencion = models.DateField(
        null=True, blank=True,default=date.today, auto_now=False, auto_now_add=False)
    usuario = models.OneToOneField("usuarios.User", related_name="usuario",blank=True,null=True, on_delete=models.CASCADE)
    banos = models.PositiveIntegerField(default=1,null=False, blank=False,verbose_name="baños")
    dormitorios = models.PositiveIntegerField(default=1,null=False, blank=False)
    zona = models.CharField(choices=zonas,null=False,blank=False,max_length=60)
    direccion = models.CharField(null=False,blank=False,max_length=60)
    estado_mantencion = models.BooleanField(default=True,null=True, blank=True)
    imagen = models.ImageField(upload_to='departamentos_principal/%Y/%m',blank=True)
    precio = models.PositiveIntegerField(default=0,null=False, blank=False)
    metros_cuadrados = models.PositiveIntegerField(default=0,null=False, blank=False)
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
    acompanantes = models.PositiveIntegerField(default=0,null=False,blank=False,verbose_name="acompañantes" )
    llegada = models.BooleanField(null=False,blank=False,default=False)
    dia_llegada = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)
    abono = models.PositiveIntegerField(null=False,blank=False )
    dias_estadia =  models.PositiveIntegerField(null=False,blank=False,verbose_name="días estadia" )
    def transporte(self):
        return self.transporte_set.filter(reserva=self.id)
    @property
    def dia_salida(self):
        return self.dia_llegada + timedelta(days=self.dias_estadia)

    @property
    def diferencia(self):
        return (self.departamento.precio * self.dias_estadia) - self.abono
    @property
    def total(self):
        return self.departamento.precio * self.dias_estadia
  
    @property
    def danos_inmuebles(self):
        inventarios = Inventario.objects.filter(departamento=self.departamento)
        total = 0 
        for inventario in inventarios:
            if inventario.estado == 'Mal estado':
                total += inventario.precio
        return total
  
    def __str__(self):
        return 'ID reserva:{} {}'.format(self.id,self.usuario)
     
class Transporte(models.Model):
    reserva = models.OneToOneField(Reserva, related_name="transporte", on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(
        null=True, blank=True, auto_now=True)
    estado_verificado = models.BooleanField(null=True,blank=True)
    precio = models.PositiveIntegerField(null=False,blank=False,default=10000)
    desde = models.CharField(null=False,blank=False,max_length=50)
    hacia =  models.CharField(null=False,blank=False,max_length=50)
    hora = models.TimeField(blank=False,null=False,auto_now=False, auto_now_add=False)
    vehiculo = models.CharField(null=False,blank=False,max_length=50)
    conductor = models.CharField(null=False,blank=False,max_length=50)
    def __str__(self):
        return '{}'.format(self.reserva.usuario)
    
class Tour(models.Model):
    departamento = models.ForeignKey(Departamento,null=True,blank=True, related_name="tour", on_delete=models.CASCADE)
    reserva = models.ManyToManyField(Reserva,blank=True, related_name="tour")
    nombre = models.CharField(null=False,blank=False,max_length=50)
    dia = models.CharField(default=date.today(),null=False,blank=False,max_length=50)
    duracion = models.PositiveIntegerField(null=False,blank=False)
    direccion = models.CharField(null=False,blank=False,max_length=50)
    precio = models.PositiveIntegerField(null=False,blank=False)
    descripcion = models.TextField(null=True)


class Arriendo(models.Model):
    reserva = models.OneToOneField(Reserva, related_name="arriendo", on_delete=models.CASCADE)
    @property
    def total_tours(self):
        reserva = Reserva.objects.filter(id=self.reserva.id).last()
        reserva_obj = Reserva.objects.get(id=reserva.id)
        total = 0

        for tour in reserva_obj.tour.all():
            total += tour.precio 
        return total   
    @property
    def transporte(self):
        transporte = 0
        if Transporte.objects.filter(reserva=self.reserva.id).exists():
            # Obtengo transporte.precio
            transporte = Transporte.objects.get(reserva=self.reserva.id)
           
        else:
         
            transporte = 0
        return transporte
    @property
    def total(self): 
        if Transporte.objects.filter(reserva=self.reserva.id).exists():
            # Obtengo transporte.precio
            trans_obj = Transporte.objects.get(reserva=self.reserva.id)
            transporte = trans_obj.precio
        else:
            transporte = 0
        total = self.total_tours + self.transporte  + self.reserva.danos_inmuebles
        return total

    def __str__(self):
        return '{}'.format(self.reserva)
class Check_in(models.Model):
    arriendo = models.OneToOneField(Arriendo, related_name="check_in", on_delete=models.CASCADE)
    diferencia = models.PositiveIntegerField(null=False,blank=False )
    total = models.PositiveIntegerField(null=False,blank=False )

class Check_out(models.Model):
    estados = (('Aceptado','Aceptado'),
            ('Rechazado','Rechazado'))
    arriendo = models.OneToOneField(Arriendo, related_name="check_out", on_delete=models.CASCADE)
    estado =  models.CharField(max_length=20,choices=estados,null=True,blank=True)
    valor_danos = models.PositiveIntegerField(null=False,blank=False,verbose_name='Valor daños' )
    valor_transporte = models.PositiveIntegerField(null=False,blank=False )
    valor_tours = models.PositiveIntegerField(null=False,blank=False )
    total = models.PositiveIntegerField(null=False,blank=False )
   

