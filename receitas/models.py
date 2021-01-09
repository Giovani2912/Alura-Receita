from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Modelo criado para cadastrar no banco python 
# Com os seguintes comandos realizamos as migrations
# manage.py makemigrations (Cria a pasta migration)
# pessoa é a chave estrangeira
class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_cozinheiro = models.CharField(max_length=200)
    especialidades = models.TextField()
    experiencias = models.TextField()
    estado = models.CharField(max_length=4)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)
    data_cozinheiro = models.DateTimeField(default=datetime.now, blank=True)
    foto_cozinheiro = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False, )

# python manage.py migrate (Executa as migrations pendentes)