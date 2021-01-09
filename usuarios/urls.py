from django.urls import path;

from . import views


# Rotas da aplicação
urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),   
    path('cadastra/cozinheiro', views.cadastra_cozinheiro, name='cadastra_cozinheiro'),   
    path('deleta/<int:receita_id>', views.deleta_cozinheiro, name='deleta_cozinheiro'), 
    path('edita/<int:receita_id>', views.edita_cozinheiro, name='edita_cozinheiro'),   
    path('atualiza_cozinheiro', views.atualiza_cozinheiro, name='atualiza_cozinheiro'),
    path('contato/<int:receita_id>', views.contato, name='contato')
]