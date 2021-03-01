from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Chamando o model receira e todos os seus objetos cadastrados no postgre
# Erro comum 



# Criando as funções junto dos templates(html) para serem reenderizados e passando alguns parâmetros para o mesmo

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request, 'index.html', dados);


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html',  receita_a_exibir);


def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)


    # Lógica para o filtro de busca
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar: 
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)