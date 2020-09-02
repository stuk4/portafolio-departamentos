from django.shortcuts import render,get_object_or_404,redirect
from departamentos.models import Departamento,ImagenesDepartamento
from django.contrib.auth.decorators import user_passes_test

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
    print(imagenes)
    context = {'departamento':departamento,
                'imagenes':imagenes}

    return render(request,'ver_departamento.html',context)
# Regla de seguridad: Solo si es funcionario o admin puede entrar al login
@user_passes_test(lambda u:u.is_staff,login_url=('login'))  
def listar_departamentos_admin(request):

    departamentos = Departamento.objects.all()
    context = {'departamentos':departamentos}

    return render(request,'lista_departamentos_admin.html',context)