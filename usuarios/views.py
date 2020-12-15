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
        receitas = Receita.objects.order_by('-data_receita').filter(
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


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']

        # Gerando o usuario e buscando o usuario da receita e a própria receita
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
        pessoa=user, 
        nome_receita=nome_receita,
        ingredientes=ingredientes,
        modo_preparo=modo_preparo,
        tempo_preparo=tempo_preparo,
        rendimento=rendimento,
        categoria=categoria,
        foto_receita=foto_receita
        )
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')