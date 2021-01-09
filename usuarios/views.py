from django.shortcuts import render, redirect, get_object_or_404
# Importando o modelo de usuários do django
from django.contrib.auth.models import User  
# Importando a autenticação/logindo django
from django.contrib import auth, messages
# Importando o modelo de receita que fizemos anteriormente
from receitas.models import Receita


# Create your views here.
def cadastro(request):
    # Buscando os dados do formulario (Lógica do cadastro)
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
            messages.error(request, 'As senhas não são iguais')
            print('Senhas diferentes')
            return redirect('cadastro')


        # Verificando se o usuário ja existe
        if User.objects.filter(email=email).exists():
            print('Usuário ja cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        
        messages.success(request, "Cadastro realizado com sucesso")
        print('Usuário cadastrado com sucesso')
        return redirect ('login')
    else:
        # essa é a primeria linha a ser digitada dentro da função, com o objetivo de renderizar a tela em chamada
        return render(request, 'usuarios/cadastro.html')



def login(request):
    # Lógica do login
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, 'Preencha todos os campos')
            print("Preencha os campos")
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    # essa é a primeria linha a ser digitada dentro da função, com o objetivo de renderizar a tela em chamada
    return render(request, 'usuarios/login.html')
    


def dashboard(request):
    if request.user.is_authenticated:     
        id = request.user.id
        receitas = Receita.objects.order_by('-data_cozinheiro').filter(
            pessoa=id
        )

        dados = {
            'receitas': receitas
        }

        # essa é a primeria linha a ser digitada dentro da função, com o objetivo de renderizar a tela em chamada
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastra_cozinheiro(request):
    if request.method == 'POST':
        nome_cozinheiro = request.POST['nome_cozinheiro']
        especialidades = request.POST['especialidades']
        experiencias = request.POST['experiencias']
        estado = request.POST['estado']
        idade = request.POST['idade']
        cidade = request.POST['cidade']
        foto_cozinheiro = request.FILES['foto_cozinheiro']

        # Gerando o usuario e buscando o usuario da receita e a própria receita
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
        pessoa=user, 
        nome_cozinheiro=nome_cozinheiro,
        especialidades=especialidades,
        experiencias=experiencias,
        estado=estado,
        idade=idade,
        cidade=cidade,
        foto_cozinheiro=foto_cozinheiro
        )
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_cozinheiro.html')


def deleta_cozinheiro(request, receita_id):
    receita = get_object_or_404(Receita, pk = receita_id)
    receita.delete()
    return redirect('dashboard')



def edita_cozinheiro(request, receita_id):
    receita = get_object_or_404(Receita, pk = receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'usuarios/edita_cozinheiro.html', receita_a_editar)


def atualiza_cozinheiro(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']

        r = Receita.objects.get(pk = receita_id)

        r.nome_cozinheiro = request.POST['nome_cozinheiro']
        r.especialidades = request.POST['especialidades']
        r.experiencias = request.POST['experiencias']
        r.estado = request.POST['estado']
        r.idade = request.POST['idade']
        r.cidade = request.POST['cidade']

        if 'foto_cozinheiro' in request.FILES:
            r.foto_cozinheiro = request.FILES['foto_cozinheiro']
        
        r.save()
        return redirect('dashboard')



def contato(request, receita_id):
    return render(request, 'usuarios/contato.html')