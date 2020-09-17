
from django.template.context_processors import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from usuarios.models import User
from departamentos.models import Reserva,Arriendo,Imagen,Departamento,Transporte
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
      
        if request.POST.get('newpass') != '':
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
    # TODO me falta agregar si esque ya esta arrenaddo tampoco tiene que mostrar la reserva
    
    # Verifico se existe un departamento relacionado con el usuario actual
    if Departamento.objects.filter(usuario=request.user.id).exists():
        # obtengo la ultima reserva hecha por el usuario actual
        reserva = Reserva.objects.filter(usuario=request.user.id).last()
        # print(Transporte.objects.get(reserva=reserva.id).estado_verificado)
        imagenes = Imagen.objects.filter(departamento=reserva.departamento.id)
        context = {'reserva':reserva,
                'imagenes':imagenes}
        if request.method == 'POST' and 'btn-acompanantes' in request.POST:
            try:
                # Aqui no uso el metodo update 
                # ya que estoy llamando aun objeto con .last()
                reserva.acompanantes = request.POST.get('acompanantes')
                reserva.save()
                messages.success(request,'Numero de acompañantes actualizado')
                return redirect('Mis reservas')
            except Exception as err:
                messages.error(request,'No se pudo actualizar')
                print('VPERFILRESERVA =====',err)
                return redirect('Mis reservas')
        
        if request.method == 'POST' and 'btn-transporte' in request.POST:
            
            if Reserva.objects.exclude(transporte__isnull=True).filter(id=reserva.id).exists():
                transporte = Transporte.objects.get(reserva=reserva.id)
     
            else:
                transporte = Transporte()
            reserva_obj = Reserva.objects.get(id=reserva.id)
            transporte.reserva =reserva_obj
            transporte.desde = request.POST.get('desde')
            transporte.hacia = request.POST.get('hacia')
            transporte.estado_verificado = None
          
            # Verifico si tiene ya un transporte
            if Reserva.objects.exclude(transporte__isnull=True).filter(id=reserva.id).exists() :
                if ransporte.objects.get(reserva=reserva.id).estado_verificado == None  :
                    messages.error(request,'Usted ya solicito un transporte')   
                    return redirect('Mis reservas')
                # elif  Transporte.objects.get(reserva=reserva.id).estado_verificado == False:
                #     pass

            try:
                transporte.save()
                messages.success(request,'Transporte solicitado ')
                return redirect('Mis reservas')
            except Exception as err:
                messages.error(request,'No se pudo solicitar el transporte')
                print('VMISRESERVASTRANSPORTE',err)
                return redirect('Mis reservas')
               
        if request.method == 'POST' and 'btn-cancelar' in request.POST:
            departamento = Departamento.objects.filter(usuario=request.user.id)
            try:
                departamento.update(usuario=None)
                messages.success(request,'Reserva cacnelada ')
                return redirect('Mis reservas')
            except Exception as err:
                print(err)
    else:
        reserva = False
        context = {'reserva':reserva}
    return render(request,'usuarios/perfil_reservas.html',context)


    # Regla de seguridad: Solo si es admin puede ver usuarios
@user_passes_test(lambda u:u.is_staff,login_url=('login'))  
def listar_usuarios(request):
    if request.resolver_match.url_name == 'Administracion usuarios':
        usuarios = User.objects.all()
    elif request.resolver_match.url_name == 'Administracion usuarios con reserva':
        usuarios = User.objects.exclude(reserva__isnull=True)

    if request.method == 'POST' and 'btn-transporte-aceptar'  in request.POST or 'btn-transporte-rechazar'  in request.POST :
        transporte = get_object_or_404(Transporte,id=request.POST.get('id-transporte'))
        if 'btn-transporte-aceptar' in request.POST:
            transporte.hora = request.POST.get('hora')
            transporte.vehiculo = request.POST.get('vehiculo')
            transporte.conductor = request.POST.get('conductor')
            transporte.estado_verificado = True
            mensaje = 'Transporte aceptado'
        elif 'btn-transporte-rechazar' in request.POST:
            transporte.estado_verificado = False
            mensaje = 'Transporte rechazado'
        try:
            transporte.save()
            messages.success(request,mensaje)
            return redirect(request.META.get('HTTP_REFERER'))
        except expression as identifier:
            messages.error(request,'No se pudo realizar la operacion')
            return redirect()
    context = {'usuarios':usuarios}
    return render(request,'usuarios/listar_usuarios_admin.html',context)
    # Regla de seguridad: Solo si es admin puede actualizar usuarios


         
@user_passes_test(lambda u:u.is_superuser,login_url=('login'))  
def actualizar_estado_usuario(request,id):
    usuario = User.objects.filter(id=id)
    # Esto lo hago para obtener los fields del model 
    check_estado =  User.objects.get(id=id)

 
    try:
        if check_estado.is_active:
            usuario.update(is_active=False)
        else:
            usuario.update(is_active=True)
        messages.success(request,'Estado de {} {} actualizado'.format(check_estado.first_name,check_estado.last_name))
        return redirect('Administracion usuarios')
        
    except Exception as err:

        messages.error(request,'No se pudo actualizar el estado')
        return redirect('Administracion usuarios')
            
   

    return redirect('Administracion usuarios')
# Fin de vistas correspondientes a parte del admin