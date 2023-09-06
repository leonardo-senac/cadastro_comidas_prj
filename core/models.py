from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Comida(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)