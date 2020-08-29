
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
            print(err)
        
    
        if user:
            login(request,user)
            
            return HttpResponseRedirect(reverse('Departamentos'))

        
        else:
           
            print('CREDENCIALES')
            messages.error(request,'Credenciales incorrectas')
            return render(request,'login.html')
    else:
     
        return render(request,'login.html')
    

def logout_view(request):
    return True