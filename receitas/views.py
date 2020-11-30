from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

# from django.http import HttpResponse
# Create your views here.

receitas = Receita.objects.all()

dados = {
    'receitas': receitas
}

def index(request):
    return render(request, 'index.html', dados);


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html',  receita_a_exibir);