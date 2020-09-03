from django.shortcuts import render,get_object_or_404,redirect
from departamentos.models import Departamento,ImagenesDepartamento,InventarioDepartamentos
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

    # Variables de para listar en mi template 
    departamentos = Departamento.objects.all()
    imagenes = ImagenesDepartamento.objects.all()
    inventarios = InventarioDepartamentos.objects.all()
    

    context = {'departamentos':departamentos,
               'imagenes':imagenes,
               'inventarios':inventarios}

    


            # Metodo post para agregar imagenes
    if request.method == 'POST' and 'btn-imagenes' in request.POST:
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

    # Metodo post para agregar inventario
    if request.method == 'POST' and 'btn-inventario' in request.POST:
        inventario = InventarioDepartamentos()
        departamento = get_object_or_404(Departamento,id=request.POST.get('idInv'))
        inventario.departamento = departamento
        inventario.nombre = request.POST.get('nombreInv')
        inventario.precio = request.POST.get('precioInv')

        try:
            inventario.save()
            messages.success(request,'Inventario {} añadido con exito'.format(request.POST.get('nombreInv')))
            return render(request,'lista_departamentos_admin.html',context)

        except Exception as err:
            print(err)
            messages.error(request,'Verifique los campos porfavor')
            return render(request,'lista_departamentos_admin.html',context)


    return render(request,'lista_departamentos_admin.html',context)
# Regla de seguridad: Solo si esadmin puede eliminar
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def eliminar_inventario_departamento(request,id):
    inventario = InventarioDepartamentos.objects.filter(id=id)
    try:
        messages.success(request,'Inventario eliminado ')
        inventario.delete()
        return redirect('Administracion departamentos')
    except Exception as err:
        print(err)
        messages.error(request,'No se pudo eliminar el inventario')
        return redirect('Administracion departamentos')
    return redirect('Administracion departamentos')
# Regla de seguridad: Solo si esadmin puede eliminar
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def eliminar_imagen_departamento(request,id):
    imagen = ImagenesDepartamento.objects.filter(id=id)
    try:
        imagen.delete()
        # messages.success(request,'Imagen {} eliminada'.format(imagen.imagen.url))
        messages.success(request,'Imagen eliminada')
        return redirect('Administracion departamentos')
    except Exception as err:
        print(err)
        # messages.error(request,'No se pudo eliminar la imagen {} '.format(imagen.imagen.url))
        messages.error(request,'No se pudo eliminar la imagen ')
        return redirect('Administracion departamentos')
    return redirect('Administracion departamentos')

def actualizar_estado_inventario(request,id):  
    
    inventario = InventarioDepartamentos.objects.filter(id=id)
    # Esto lo hago para obtener los fields del model 
    check_estado =  InventarioDepartamentos.objects.get(id=id)

    if check_estado.estado == 'Buen estado':
        try:

            inventario.update(estado='Mal estado')
            messages.success(request,'Estado de  {} actualizado'.format(check_estado.nombre))
            return redirect('Administracion departamentos')
            
        except Exception as err:

            messages.error(request,'No se pudo actualizar el estado')
            return redirect('Administracion departamentos')
            
    else:
        try:

            inventario.update(estado='Buen estado')
            messages.success(request,'Estado de  {} actualizado'.format(check_estado.nombre))
            return redirect('Administracion departamentos')

        except Exception as err:

            print(err)
            messages.error(request,'No se pudo actualizar el estado')
            return redirect('Administracion departamentos')

    return redirect('Administracion departamentos')
    