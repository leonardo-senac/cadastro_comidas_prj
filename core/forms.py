from django import forms
from .models import *

class FormCategoria(forms.Form):
    nome = forms.CharField(label='Nome da categoria', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nome...'}))

class FormComida(forms.Form):
    nome = forms.CharField(label='Nome da comida', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nome...'}))
    descricao = forms.CharField(label='Descrição da comida', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Descrição...'}))
    estoque = forms.IntegerField(label='Estoque')
    preco = forms.DecimalField(max_digits=10, decimal_places=2, label='Preço')
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())