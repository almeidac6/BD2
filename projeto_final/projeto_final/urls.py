"""
URL configuration for projeto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loja import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('armazens/', views.listar_armazens, name='listar_armazens'),
    path('armazens/adicionar/', views.adicionar_armazem, name='adicionar_armazem'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('funcionarios/adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('veiculos/adicionar/', views.adicionar_veiculo, name='adicionar_veiculo'),
    path('login/cliente/', views.login_cliente, name='login_cliente'),
    path('login/funcionario/', views.login_funcionario, name='login_funcionario'),
    path('loja', views.listar_produtos_c, name='loja'),


    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('remover_carrinho/<int:item_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra')
]

