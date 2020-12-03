from django.contrib import admin
from .models import Receita

# As seguintes alterações são feitas para o uso único e exclusivo do admnistrador do site

# Criamos uma classe para que o crud do admin não fique faltando informações, por exemplo: de object1 ele foi para id + nome_receita
# Para passarmos os parâmetros a serem atribuidos na interface do django-admin, usaremos o método list_display ou exibição de tela
# E para tornarmos os mesmos clicaveis, usamos o list_display_links
# Para o admin utilizar o campo de buscas, passamos o "search_fields" e o parâmetro para ser encontrado


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 5


# Devemos registrar nossos models e classes, para que o django-admin tenha acesso aos mesmos
admin.site.register(Receita, ListandoReceitas)