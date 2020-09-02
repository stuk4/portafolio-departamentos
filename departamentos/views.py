from django.shortcuts import render,get_object_or_404,redirect
from departamentos.models import Departamento,ImagenesDepartamento
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
def listar_departamentos(request):
    # Se es administrador o funcionario redirecciona al sitio administracion
    if request.user.is_staff:

        return redirect('Administracion departamentos')
    # De lo contrario al sitio normal
    else:
        departamentos = Departamento.objects.filter(estado_mantencion=False)
        context = {'departamentos':departamentos}

        return render(request,'lista_departamentos.html',context)

def ver_departamento(request,id):

    departamento = get_object_or_404(Departamento,id=id)
    imagenes = ImagenesDepartamento.objects.filter(departamento=id)
  
    context = {'departamento':departamento,
                'imagenes':imagenes}

    return render(request,'ver_departamento.html',context)
# Regla de seguridad: Solo si es  admin puede entrar
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def listar_departamentos_admin(request):
    departamentos = Departamento.objects.all()
    imagenes = ImagenesDepartamento.objects.all()
    context = {'departamentos':departamentos,
               'imagenes':imagenes}
    if request.method == 'POST':
        imagen = ImagenesDepartamento()
        
        departamento = get_object_or_404(Departamento,id=request.POST.get('idDep'))

        imagen.departamento = departamento
        
        imagen.imagen = request.FILES.get('imagenDep')
        
        if request.FILES.get('imagenDep') == None:
            messages.error(request,'Verifique los campos porfavor')
            return render(request,'lista_departamentos_admin.html',context)
       

        try:
            imagen.save()
            messages.success(request,'Imagen añadida con exito')
            return render(request,'lista_departamentos_admin.html',context)
        except Exception as err:
            print(err)
            messages.error(request,'Lo sentimos hubo un error')
            return render(request,'lista_departamentos_admin.html',context)
    

    return render(request,'lista_departamentos_admin.html',context)

# Regla de seguridad: Solo si esadmin puede eliminar
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def eliminar_imagen_departamento(request,id):
    imagen = ImagenesDepartamento.objects.filter(id=id)
    try:
        imagen.delete()
        # messages.success(request,'Imagen {} eliminada'.format(imagen.imagen.name))
        messages.success(request,'Imagen eliminada')
        return redirect('Administracion departamentos')
    except Exception as err:
        print(err)
        # messages.error(request,'No se pudo eliminar la imagen {} '.format(imagen.imagen.name))
        messages.error(request,'No se pudo eliminar la imagen ')
        return redirect('Administracion departamentos')
    return redirect('Administracion departamentos')