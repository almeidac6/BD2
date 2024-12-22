# loja/forms.py

from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'password']

class ArmazemForm(forms.ModelForm):
    class Meta:
        model = Armazem
        fields = ['localizacao', 'capacidade']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['id_armazem', 'nome', 'preco', 'descricao']

    # Adicionando o campo para selecionar o armazém
    id_armazem = forms.ChoiceField(
        choices=[(armazem.id_armazem, armazem.localizacao) for armazem in Armazem.objects.using('mongo').all()],
        required=True,
        label="Selecione o Armazém"
    )

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'telefone', 'email', 'password']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['matricula', 'modelo']