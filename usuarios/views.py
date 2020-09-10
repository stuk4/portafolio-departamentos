
from django.template.context_processors import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from usuarios.models import User
from django.contrib.auth.decorators import user_passes_test
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

def perfil(request):
    return render(request,'usuarios/perfil.html')
