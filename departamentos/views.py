from django.shortcuts import render,get_object_or_404
from departamentos.models import Departamento,ImagenesDepartamento
# Create your views here.
from django.contrib.auth.decorators import user_passes_test

def listar_departamentos(request):
    departamentos = Departamento.objects.filter(estado_mantencion=False)
    context = {'departamentos':departamentos}
    return render(request,'lista_departamentos.html',context)

def ver_departamento(request,id):
    departamento = get_object_or_404(Departamento,id=id)
    imagenes = ImagenesDepartamento.objects.filter(departamento=id)
    print(imagenes)
    context = {'departamento':departamento,
                'imagenes':imagenes}
    return render(request,'ver_departamento.html',context)