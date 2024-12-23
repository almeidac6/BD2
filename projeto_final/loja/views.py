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
    carrinho = request.POST.get('carrinho')
    if carrinho:
        carrinho = json.loads(carrinho)
    else:
        carrinho = []

    # Calcular o total
    total = sum(item['preco'] * item['quantidade'] for item in carrinho)

    return render(request, 'checkout.html', {
        'carrinho': carrinho,
        'total': total
    })

def checkout_final(request):
    if request.method == 'POST':
        # Recuperar o carrinho do POST
        carrinho_data = request.POST.get('carrinho')
        if not carrinho_data:
            return HttpResponse("Carrinho vazio", status=400)

        carrinho = json.loads(carrinho_data)

        # Capturar os dados do formulário
        cliente_id = request.session.get('cliente_id')
        morada = "meow"

        # Criar a encomenda
        encomenda = Encomendas.objects.create(
            idcliente=cliente_id,
            morada=morada,
        )

        # Adicionar os itens ao banco de dados
        for item in carrinho:
            produto = Produto.objects.using('mongo').get(id_produto=item['id'])
            ItemEncomenda.objects.create(
                encomenda=encomenda.idencomendas,
                produto=produto.id_produto,
                quantidade=item['quantidade'],
                preco=item['preco']
            )

        return redirect('sucesso')  # Redirecionar para uma página de sucesso

    return render(request, 'checkout_final.html')

def sucesso(request):
    return render(request, 'sucesso.html')


from django.shortcuts import render, redirect
from .models import Encomendas, Pagamentos

from django.shortcuts import render, redirect
from .models import Encomendas, Pagamentos


def pagamentos_pendentes(request):
    if 'cliente_id' not in request.session:
        return redirect('login_cliente')

    # Buscar todas as encomendas do cliente logado
    encomendas = Encomendas.objects.filter(idcliente=request.session.get('cliente_id'))

    pagamentos = []

    for encomenda in encomendas:
        # Buscar itens relacionados à encomenda com base no id da encomenda
        itens = ItemEncomenda.objects.filter(
            encomenda=encomenda.idencomendas)  # Usando o id da encomenda para buscar os itens

        # Verificar se há algum pagamento relacionado à encomenda
        pagamento_existe = Pagamentos.objects.filter(idencomendas=encomenda.idencomendas).exists()

        # Se não houver pagamento relacionado, adicionar a encomenda com seus itens
        if not pagamento_existe:
            pagamentos.append({
                'encomenda': encomenda,
                'itens': itens
            })

    return render(request, 'pagamentos_pendentes.html', {
        'pagamentos': pagamentos
    })

def detalhes_pagamento(request, idencomenda):
    # Buscar a encomenda específica com base no ID da encomenda
    encomenda = get_object_or_404(Encomendas, idencomendas=idencomenda)

    # Buscar os itens da encomenda relacionada
    itens_encomenda = ItemEncomenda.objects.filter(encomenda=idencomenda)

    # Exibir os detalhes na página
    return render(request, 'detalhes_pagamento.html', {
        'encomenda': encomenda,
        'itens_encomenda': itens_encomenda,
    })

def registrar_pagamento(request, idencomenda):
    # Verificar se o cliente está autenticado
    if 'cliente_id' not in request.session:
        return redirect('login_cliente')

    # Buscar a encomenda com base no ID
    encomenda = get_object_or_404(Encomendas, idencomendas=idencomenda)

    # Verificar se já existe um pagamento registrado para a encomenda
    if Pagamentos.objects.filter(idencomendas=encomenda).exists():
        return render(request, 'erro_pagamento.html', {'message': 'Pagamento já registrado para esta encomenda.'})

    # Registrar o pagamento
    pagamento = Pagamentos(
        idencomendas=encomenda.idencomendas,
        data=timezone.now(),
        valor=10,  # Supondo que você tenha uma função que calcula o total da encomenda
        metodo="Cartão de Crédito",  # Exemplo de método, isso pode ser alterado conforme a lógica do seu sistema
    )
    pagamento.save()

    # Redirecionar para a página de detalhes do pagamento ou para outra página de sucesso
    return redirect('detalhes_pagamento', idencomenda)