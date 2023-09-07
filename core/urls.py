from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_comida/', cadastrar_comida, name='cadastrar_comida'),
    path('home/', home, name='home'),
    path('excluir_comida/<int:id_comida>/', excluir_comida, name='excluir_comida'),
    path('cadastrar_categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    path('exibir_categoria/', exibir_categorias, name='exibir_categorias'),
    path('excluir_categoria/<int:id_categoria>/', excluir_categoria, name='excluir_categoria'),
    path('comidas_por_categorias/<int:id_categoria>', comidas_por_categoria, name='comidas_por_categoria'),
    path('editar_categoria/<int:id_categoria>/', editar_categoria, name='editar_categoria')
]