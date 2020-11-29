from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.

receitas = {
    1:'Parmegiana',
    2:'Escondidinho',
    3:'Tapioca',
    4:'Omelete'
}

dados = {
    'nome_das_receitas': receitas
}

def index(request):
    return render(request, 'index.html', dados);


def receita(request):
    return render(request, 'receita.html');