from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .util import *

def dashboard(request):
    return render(request, 'dashboard.html')

def listar_clientes(request):
    clientes = Cliente.objects.using('mongo').all()  # Busca todos os dados da tabela Cliente
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.id_cliente = generate_uuid_srt()
            cliente.save()
            return redirect('registo_sucesso')  # Redireciona para uma página de sucesso após o registro
    else:
        form = ClienteForm()

    return render(request, 'adicionar_cliente.html', {'form': form})

def listar_armazens(request):
    armazens = Armazem.objects.using('mongo').all()  # Obtém todos os armazéns
    return render(request, 'listar_armazens.html', {'armazens': armazens})

def adicionar_armazem(request):
    if request.method == 'POST':
        form = ArmazemForm(request.POST)
        if form.is_valid():
            armazem = form.save(commit=False)  # Não salva ainda
            armazem.id_armazem = generate_uuid_srt()  # Atribui um id único ao armazém
            armazem.save()  # Salva no MongoDB
            return redirect('listar_armazens')  # Redireciona para a lista de armazéns
    else:
        form = ArmazemForm()

    return render(request, 'adicionar_armazem.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.using('mongo').all()  # Obtém todos os produtos
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)  # Não salva ainda
            produto.id_produto = generate_uuid_srt()  # Atribui um id único ao produto
            produto.save()  # Salva no MongoDB
            return redirect('produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm()

    return render(request, 'adicionar_produto.html', {'form': form})

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.using('mongo').all()
    return render(request, 'listar_funcionarios.html', {'funcionarios': funcionarios})

def adicionar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.id_funcionario = generate_uuid_srt()  # Gera o ID único para o funcionário
            funcionario.save()  # Salva no MongoDB
            return redirect('listar_funcionarios')  # Redireciona para a lista de funcionários
    else:
        form = FuncionarioForm()

    return render(request, 'adicionar_funcionario.html', {'form': form})

def listar_veiculos(request):
    veiculos = Veiculo.objects.using('mongo').all()
    return render(request, 'listar_veiculos.html', {'veiculos': veiculos})

def adicionar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            veiculo = form.save(commit=False)
            veiculo.id_veiculo = generate_uuid_srt()  # Gera o ID único para o veículo
            veiculo.save()  # Salva no MongoDB
            return redirect('listar_veiculos')  # Redireciona para a lista de veículos
    else:
        form = VeiculoForm()

    return render(request, 'adicionar_veiculo.html', {'form': form})