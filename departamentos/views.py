from django.shortcuts import render
from departamentos.models import Departamento
# Create your views here.
from django.contrib.auth.decorators import user_passes_test
@user_passes_test(lambda u:u.is_active,login_url=('login'))  
def listar_departamentos(request):
    departamentos = Departamento.objects.filter(estado_mantencion=False)
    context = {'departamentos':departamentos}
    return render(request,'lista_departamentos.html',context)