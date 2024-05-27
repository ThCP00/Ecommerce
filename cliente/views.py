from django.shortcuts import render, redirect
from .models import Perfil
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def salvar_perfil(request):
    if request.method == 'POST':
        cep = request.POST['cep']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        perfil = Perfil(usuario=request.user, cep=cep, cpf=cpf, telefone=telefone)
        perfil.save()
        return redirect('/')

def perfil(request):
    return render(request, 'perfil.html')




