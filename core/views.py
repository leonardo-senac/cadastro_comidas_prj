from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def cadastrar_comida(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        # Abrindo a carta
        nome_comida = request.POST['nome_comida']
        descricao_comida = request.POST['descricao_comida']
        estoque = request.POST['estoque']
        preco = request.POST['preco']
        id_categoria = request.POST['id_categoria']
        categoria = Categoria.objects.get(id=id_categoria)

        # Salvando no banco de dados
        Comida.objects.create(nome=nome_comida, descricao=descricao_comida, estoque=estoque, preco=preco, categoria=categoria)

    return render(request, 'cadastro_comida.html', {'categorias': categorias})

def home(request):
    comidas = Comida.objects.all()
    return render(request, 'home.html', {'comidas': comidas})

def excluir_comida(request, id_comida):
    comida = Comida.objects.get(id=id_comida)

    comida.delete()

    return redirect(home)

def cadastrar_categoria(request):
    if request.method == 'POST':
        # Abrindo a carta
        nome_categoria = request.POST['nome_categoria']

        # Salvando no banco de dados
        Categoria.objects.create(nome=nome_categoria)

    return render(request, 'cadastro_categoria.html')

def exibir_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'categorias.html', {'categorias': categorias})

def excluir_categoria(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)

    categoria.delete()

    return redirect(exibir_categorias)

def comidas_por_categoria(request, id_categoria):
    categoria_puxada = Categoria.objects.get(id=id_categoria)

    comidas = Comida.objects.filter(categoria=categoria_puxada)

    return render(request, 'home.html', {'comidas': comidas})