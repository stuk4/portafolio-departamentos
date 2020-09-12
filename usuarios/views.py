
from django.template.context_processors import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from usuarios.models import User
from departamentos.models import Reserva,Arriendo,Imagen
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.password_validation import MinimumLengthValidator,NumericPasswordValidator,CommonPasswordValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash
# Regla de segurdad: Solo si es anonimo puede entrar al login
@user_passes_test(lambda u:u.is_anonymous,login_url=('Departamentos'))  
def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['email'].lower()
        password = request.POST['password']
        try:
            user = authenticate(request,username = username, password = password)
            
        except Exception as err:
            messages.error(request,'Lo sentimos hubo un problema')
            return render(request,'usuarios/login.html')
        
    
        if user:
            login(request,user)
            messages.info(request,'Bienvenid@ {}'.format(request.user.first_name))
            return HttpResponseRedirect(reverse('Departamentos'))

        
        else:
         
            messages.error(request,'Credenciales incorrectas')
            return render(request,'usuarios/login.html')
    else:
        if request.user.is_active:

            messages.info(request,'Bienvenido {}'.format(request.user.first_name))
        return render(request,'usuarios/login.html')


        
# Regla de segurdad: Solo si es activo puede hacer post logout
@user_passes_test(lambda u:u.is_active,login_url=('Departamentos'))  
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        
    return redirect('login')


# Regla de segurdad: Solo si es anonimo puede ver registro
@user_passes_test(lambda u:u.is_anonymous,login_url=('Departamentos'))  
def registro(request):
    
    if request.method == 'POST':
        try:
            validadores = [MinimumLengthValidator,NumericPasswordValidator,CommonPasswordValidator]
            for validador in validadores:
                validador().validate(request.POST.get('password'))
        except ValidationError as e:
            messages.error(request,str(e).replace("'", "").replace("[","").replace("]",""))
            return render(request,'usuarios/Registro.html')
            
        try:
           
            user = User.objects.create_user(username=request.POST['email'],password=request.POST['password'],is_active=True)

        except:
            messages.error(request,'Usuario ya registrado')
            return render(request,'usuarios/Registro.html')
       
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('lastname')
        user.telefono = request.POST.get('phone')
        user.fecha_nacimiento = request.POST.get('date')
        user.N_tarjeta = request.POST.get('card')
        try:
           
            user.save()
            messages.success(request,'Registrado con exito')
            return render(request,'usuarios/Registro.html')
        except Exception as err:
            context = {'alerta':'ok-alerta'}
            messages.error(request,'Verifique los campos porfavor')
            print(err)
            return render(request,'usuarios/Registro.html')
    
    return render(request,'usuarios/Registro.html')
# Regla de segurdad: Solo si es activo puede ver 
@user_passes_test(lambda u:u.is_active,login_url=('Departamentos'))
def perfil(request):

    usuario = get_object_or_404(User,id=request.user.id)
    
    if request.method == 'POST':
        if request.FILES.get('imagenperfil') is None:
            usuario.imagen = usuario.imagen
        else:
            usuario.imagen = request.FILES.get('imagenperfil')
        usuario.first_name = request.POST.get('nombres')
        usuario.last_name = request.POST.get('apellidos')
        usuario.telefono = request.POST.get('telefono')
        if usuario.check_password(request.POST.get('oldpass')) is False:
            messages.error(request,'Esa no es su contraseña')
            return redirect('Perfil')
        validadores = [MinimumLengthValidator,NumericPasswordValidator,CommonPasswordValidator]
      
        if request.POST.get('newpass') is not '':
            try:
                for validador in validadores:
                    validador().validate(request.POST.get('newpass'))
            except ValidationError as e:
                messages.error(request,str(e).replace("'", "").replace("[","").replace("]",""))
                return redirect('Perfil')
            usuario.set_password(request.POST.get('newpass'))
        try:
            usuario.save()
            update_session_auth_hash(request,usuario)
            messages.success(request,'Perfil acualizado con exito')
            return redirect('Perfil')
        except Exception as err:
            print('VPERFIL ---',err)
            messages.error(request,'No se pudo actualizar su perfil')
            return redirect('Perfil')
        
    return render(request,'usuarios/perfil.html')

def perfil_reservas(request):
    reserva = Reserva.objects.get(usuario=request.user.id)
    reserva_u  = Reserva.objects.filter(usuario=request.user.id)
    imagenes = Imagen.objects.filter(departamento=reserva.departamento.id)
    if request.method == 'POST' and 'btn-acompanantes' in request.POST:
        try:
            reserva_u.update(acompanantes=request.POST.get('acompanantes'))
            messages.success(request,'Numero de acompañantes actualizado')
            return redirect('Mis reservas')
        except Exception as err:
            messages.error(request,'No se pudo actualizar')
            print('VPERFILRESERVA =====',err)
            return redirect('Mis reservas')
    context = {'reserva':reserva,
              'imagenes':imagenes}
    return render(request,'usuarios/perfil_reservas.html',context)
