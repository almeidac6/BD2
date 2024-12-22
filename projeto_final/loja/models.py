from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=9)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    class Meta:
        db_table = 'clientes'
        app_label = 'loja'

    def save(self, *args, **kwargs):
        super(Cliente, self).save(using='mongo', *args, **kwargs)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    id_produto = models.CharField(max_length=50, primary_key=True)
    id_armazem = models.CharField(max_length=50)  # FK relacionamento com Armazem
    nome = models.CharField(max_length=250)
    preco = models.FloatField()
    descricao = models.CharField(max_length=250)

    class Meta:
        db_table = 'produtos'
        app_label = 'loja'

    def save(self, *args, **kwargs):
        super(Produto, self).save(using='mongo', *args, **kwargs)

    def __str__(self):
        return self.nome


class Armazem(models.Model):
    id_armazem = models.CharField(max_length=50, primary_key=True)
    localizacao = models.CharField(max_length=250)
    capacidade = models.IntegerField()

    class Meta:
        db_table = 'armazem'
        app_label = 'loja'

    def save(self, *args, **kwargs):
        super(Armazem, self).save(using='mongo', *args, **kwargs)

    def __str__(self):
        return self.localizacao


class Funcionario(models.Model):
    id_funcionario = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=9)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    class Meta:
        db_table = 'funcionario'
        app_label = 'loja'

    def save(self, *args, **kwargs):
        super(Funcionario, self).save(using='mongo', *args, **kwargs)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    id_veiculo = models.CharField(max_length=50, primary_key=True)
    matricula = models.CharField(max_length=250)
    modelo = models.CharField(max_length=250)

    class Meta:
        db_table = 'veiculos'
        app_label = 'loja'

    def save(self, *args, **kwargs):
        super(Veiculo, self).save(using='mongo', *args, **kwargs)

    def __str__(self):
        return self.modelo
