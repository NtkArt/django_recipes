from django.shortcuts import render
from .models import Receitas

# Create your views here.


def index(request):

    receitas = Receitas.objects.all()
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    return render(request, 'receita.html')
