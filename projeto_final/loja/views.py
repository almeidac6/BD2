from django.shortcuts import *
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.contrib.auth.hashers import *
from django.contrib import *
from django.http import *
from django.utils import *
from .models import *
from .forms import *
from .util import *
import json

def dashboard(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    return render(request, 'dashboard.html')

def listar_clientes(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    clientes = Cliente.objects.using('mongo').all()  # Busca todos os dados da tabela Cliente
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def adicionar_cliente(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.id_cliente = generate_uuid_srt()
            cliente.save()
            return redirect('listar_clientes')  # Redireciona para uma página de sucesso após o registro
    else:
        form = ClienteForm()

    return render(request, 'adicionar_cliente.html', {'form': form})

def listar_armazens(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    armazens = Armazem.objects.using('mongo').all()  # Obtém todos os armazéns
    return render(request, 'listar_armazens.html', {'armazens': armazens})

def adicionar_armazem(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

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
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    produtos = Produto.objects.using('mongo').all()  # Obtém todos os produtos
    armazens = Armazem.objects.using('mongo').all()
    return render(request, 'listar_produtos.html', {'produtos': produtos, 'armazens': armazens})

def adicionar_produto(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)  # Não salva ainda
            produto.id_produto = generate_uuid_srt()  # Atribui um id único ao produto
            produto.save()  # Salva no MongoDB
            return redirect('listar_produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm()

    return render(request, 'adicionar_produto.html', {'form': form})

def listar_funcionarios(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    funcionarios = Funcionario.objects.using('mongo').all()
    return render(request, 'listar_funcionarios.html', {'funcionarios': funcionarios})

def adicionar_funcionario(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

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
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    veiculos = Veiculo.objects.using('mongo').all()
    return render(request, 'listar_veiculos.html', {'veiculos': veiculos})

def adicionar_veiculo(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

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


def login_cliente(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            cliente = Cliente.objects.using('mongo').get(email=email)
            if cliente.password == password:  # Manually check password
                request.session['cliente_id'] = cliente.id_cliente
                request.session['cliente_nome'] = cliente.nome
                messages.success(request, f"Bem-vindo, {cliente.nome}!")
                return redirect('loja')
            else:
                messages.error(request, "Senha incorreta. Tente novamente.")
        except Cliente.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")

    return render(request, 'login_cliente.html')


def login_funcionario(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            funcionario = Funcionario.objects.using('mongo').get(email=email)
            if funcionario.password == password:  # Validação simples
                request.session['funcionario_id'] = funcionario.id_funcionario
                request.session['funcionario_nome'] = funcionario.nome
                messages.success(request, f"Bem-vindo, {funcionario.nome}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Senha incorreta.")
        except Funcionario.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")

    return render(request, 'login_funcionario.html')

def loja(request):
    if 'cliente_id' not in request.session:
        return redirect('login_cliente')

    produtos = Produto.objects.using('mongo').all()  # Obtém todos os produtos da loja

    # Recupera o carrinho da sessão, caso exista
    carrinho = request.session.get('carrinho', [])

    return render(request, 'loja.html', {'produtos': produtos, 'carrinho': carrinho})


def checkout(request):
    if request.method == 'POST':
        # Verifica os dados do carrinho no POST
        try:
            carrinho_data = request.POST.get('carrinho')
            if carrinho_data:
                carrinho = json.loads(carrinho_data)

                # Armazena os itens no carrinho da sessão
                request.session['carrinho'] = carrinho

                # Redireciona para a página de confirmação
                return redirect('checkout_final')

        except Exception as e:
            print(f"Erro ao processar o carrinho: {e}")
            messages.error(request, "Erro ao processar o carrinho.")
            return redirect('erro')

    return render(request, 'checkout.html')  # Substitua pelo seu template


def checkout_final(request):
    # Recupera os dados do carrinho da sessão
    carrinho = request.session.get('carrinho', [])

    # Caso o carrinho esteja vazio ou não exista
    if not carrinho:
        messages.error(request, "Carrinho vazio ou não encontrado.")
        return redirect('loja')  # Redireciona para a loja se o carrinho estiver vazio

    if 'carrinho' in request.session:
        del request.session['carrinho']

    # Aqui você pode processar o pagamento ou realizar outras ações

    # Exibe os dados do carrinho na página de confirmação
    return render(request, 'checkout_final.html', {'carrinho': carrinho})