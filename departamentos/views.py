from django.shortcuts import render,get_object_or_404,redirect
from departamentos.models import Departamento,Imagen,Inventario
from usuarios.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


#  Views correspondientes a vistas del cliente
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
    imagenes = Imagen.objects.filter(departamento=id)
  
    context = {'departamento':departamento,
                'imagenes':imagenes}

    return render(request,'ver_departamento.html',context)

# Fin de vistas corrrespondientes a parte del cliente


# Vistas correspondientes parte del admin
# Regla de seguridad: Solo si es  admin puede entrar
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def listar_departamentos_admin(request):

    # Variables de para listar en mi template 
    departamentos = Departamento.objects.all()
    imagenes = Imagen.objects.all()
    inventarios = Inventario.objects.all()
    

    context = {'departamentos':departamentos,
               'imagenes':imagenes,
               'inventarios':inventarios}

    


    # Metodo post para agregar imagenes
    if request.method == 'POST' and 'btn-imagenes' in request.POST:
        imagen = Imagen()
        
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
        inventario = Inventario()
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
    inventario = Inventario.objects.filter(id=id)
    try:
        messages.success(request,'Inventario eliminado ')
        inventario.delete()
        return redirect('Administracion departamentos')
    except Exception as err:
        print(err)
        messages.error(request,'No se pudo eliminar el inventario')
        return redirect('Administracion departamentos')
    return redirect('Administracion departamentos')

# Regla de seguridad: Solo si es admin puede eliminar
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def eliminar_imagen_departamento(request,id):
    imagen = Imagen.objects.filter(id=id)
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


# Regla de seguridad: Solo si es admin puede actualizar estado
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def actualizar_estado_inventario(request,id):  
    
    inventario = Inventario.objects.filter(id=id)
    # Esto lo hago para obtener los fields del model 
    check_estado =  Inventario.objects.get(id=id)

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
    # Regla de seguridad: Solo si es admin puede ver usuarios
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def listar_usuarios(request):
    usuarios = User.objects.all()
    context = {'usuarios':usuarios}
    return render(request,'listar_usuarios_admin.html',context)

def actualizar_estado_usuario(request,id):
    usuario = User.objects.filter(id=id)
    # Esto lo hago para obtener los fields del model 
    check_estado =  User.objects.get(id=id)
    if check_estado.is_active:
 
        try:

            usuario.update(is_active=False)
            messages.success(request,'Estado de {} {} actualizado'.format(check_estado.first_name,check_estado.last_name))
            return redirect('Administracion usuarios')
            
        except Exception as err:

            messages.error(request,'No se pudo actualizar el estado')
            return redirect('Administracion usuarios')
            
    else:
        try:

            usuario.update(is_active=True)
            messages.success(request,'Estado de {} {} actualizado'.format(check_estado.first_name,check_estado.last_name))
            return redirect('Administracion usuarios')

        except Exception as err:

            print(err)
            messages.error(request,'No se pudo actualizar el estado')
            return redirect('Administracion usuarios')

    return redirect('Administracion usuarios')
# Fin de vistas correspondientes a parte del admin