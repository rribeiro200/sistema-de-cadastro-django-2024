# Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse
# Models
from .models import Usuario


# Create your views here.
def home(request):
    # TODO: Renderizar um formulário Django para html HOME

    return render(
        request,
        'usuarios/home.html',
    )


def cria_usuarios(request):
    new_user = Usuario()

    if not request.POST:
        return HttpResponse('Requisição inválida!')
    
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()

    return redirect(reverse('cadastro_usuarios:lista_usuarios'))


def lista_usuarios(request):
    user = Usuario.objects.all()

    ctx = {
        'usuarios': user
    }

    return render(
        request,
        'usuarios/usuarios.html',
        context=ctx
    )


def deleta_usuarios(request, pk):
    user = Usuario.objects.filter(pk=pk).first()
    user.delete() #type: ignore

    return redirect(reverse('cadastro_usuarios:lista_usuarios'))