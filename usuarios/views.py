from django.shortcuts import render, redirect
# Importando o modelo de usuários do django
from django.contrib.auth.models import User  
# Create your views here.
def cadastro(request):
    # Buscando os dados do formulario
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        # Validações:
        # retirando a possibilidade de deixar o nome e o email em branco

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect ('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect ('cadastro')


        # Verificando se a senha é igual a confirmação
        if senha != senha2:
            print('Senhas diferentes')
            return redirect('cadastro')


        # Verificando se o usuário ja existe
        if User.objects.filter(email=email).exists():
            print('Usuário ja cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        

        print('Usuário cadastrado com sucesso')
        return redirect ('login')
    else:
        return render(request, 'usuarios/cadastro.html')



def login(request):
    return render(request, 'usuarios/login.html')
    


def dashboard(request):
    pass


def logout(request):
    pass


