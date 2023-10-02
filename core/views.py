from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect(home)
    else:
        form = AuthenticationForm()
    return render(request, 'logar.html', {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(logar)
    else:
        form = UserCreationForm()

    return render(request, 'cadastrar.html', {'form': form})

def cadastrar_comida(request):
    form = FormComida()
    if request.method == 'POST':
        # Abrindo a carta
        form = FormComida(request.POST)
        if form.is_valid():
            nome_comida = form.cleaned_data['nome']
            descricao_comida = form.cleaned_data['descricao']
            estoque = form.cleaned_data['estoque']
            preco = form.cleaned_data['preco']
            categoria = form.cleaned_data['categoria']

            # Salvando no banco de dados
            Comida.objects.create(nome=nome_comida, descricao=descricao_comida, estoque=estoque, preco=preco, categoria=categoria)

    return render(request, 'cadastro_comida.html', {'form': form})

def home(request):
    comidas = Comida.objects.all()
    return render(request, 'home.html', {'comidas': comidas})

def excluir_comida(request, id_comida):
    comida = Comida.objects.get(id=id_comida)

    comida.delete()

    return redirect(home)

def cadastrar_categoria(request):
    form = FormCategoria()
    if request.method == 'POST':
        form = FormCategoria(request.POST)
        if form.is_valid():
            # Abrindo a carta
            nome_categoria = form.cleaned_data['nome_categoria']
            # Salvando no banco de dados
            Categoria.objects.create(nome=nome_categoria)

    return render(request, 'cadastro_categoria.html', {'form': form})

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

def editar_categoria(request, id_categoria):
    categoria_puxada = Categoria.objects.get(id=id_categoria)

    if request.method == 'POST':
        categoria_puxada.nome = request.POST['nome_categoria']
        categoria_puxada.save()
        return redirect(exibir_categorias)

    return render(request, 'editar_categoria.html', {'categoria': categoria_puxada})

def editar_comida(request, id_comida):
    categorias = Categoria.objects.all()
    comida = Comida.objects.get(id=id_comida)
    if request.method == "POST":
        comida.nome = request.POST['nome_comida']
        comida.descricao = request.POST['descricao_comida']
        comida.estoque = request.POST['estoque']
        comida.preco = request.POST['preco']
        comida.categoria = Categoria.objects.get(id=request.POST['id_categoria'])

        comida.save()

    return render(request, 'editar_comida.html', {'comida': comida, 'categorias': categorias})