from django.shortcuts import render
from .models import Usuarios
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'usuarios/home.html')

def login(request):
    username = request.POST[new_user.email]
    password = request.POST[new_user.password]
    user = authenticate(request, username=username, password=password)
    if user is not none:
        return render(request, 'usuarios/usuarios.html',usuarios)
    else:
        return render(request, "usuarios/login_error.html")



def usuarios(request):
    # Salvar  os dados da tela para o banco de dados.
    new_user = Usuarios()
    new_user.firstname = request.POST.get('firstname')
    new_user.lastname = request.POST.get('lastname')
    new_user.email = request.POST.get('email')
    new_user.number = request.POST.get('number')
    new_user.password = request.POST.get('password')
    new_user.confirm_password = request.POST.get('confirm_password')
    new_user.gender_choices = request.POST.get('gender')
    new_user.gender = request.POST.get('gender')
    new_user.save()
    # Exibir todosos usuários já cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)

