from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita



# Chamando o model receira e todos os seus objetos cadastrados no postgre
receitas = Receita.objects.all()

dados = {
    'receitas': receitas
}


# Criando as funções junto dos templates(html) para serem reenderizados e passando alguns parâmetros para o mesmo

def index(request):
    return render(request, 'index.html', dados);


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html',  receita_a_exibir);