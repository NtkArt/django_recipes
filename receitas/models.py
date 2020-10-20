from django.db import models
from datetime import datetime
# Create your models here.


class Receitas(models.Model):
    nome_receita = models.CharField(max_length=256)
    ingredientes = models.TextField(max_length=500)
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=120)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
