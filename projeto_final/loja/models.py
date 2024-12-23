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
        if not self.pk and self.password:  # Se a senha for fornecida e o cliente não tem um ID ainda
            self.password = make_password(self.password)  # Criptografa a senha
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

####### POSTGRES

class Encomendas(models.Model):
    idencomendas = models.AutoField(primary_key=True)
    idcliente = models.CharField(max_length=250)
    morada = models.CharField(max_length=250)
    datacriacao = models.CharField(max_length=250)
    status = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'encomendas'

class ItemEncomenda(models.Model):
    iditemencomenda = models.AutoField(primary_key=True)
    encomenda = models.CharField(max_length=250)
    produto = models.CharField(max_length=250)
    quantidade = models.CharField(max_length=250)
    preco = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'item_encomenda'

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} x {self.preco}€'


class Entregas(models.Model):
    identregas = models.AutoField(primary_key=True)
    idpagamentos = models.CharField(max_length=250)
    idfuncionario = models.CharField(max_length=250)
    idveiculo = models.CharField(max_length=250)
    data = models.CharField(max_length=250)
    situacao = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'entregas'

class Pagamentos(models.Model):
    idpagamentos = models.AutoField(primary_key=True)
    idencomendas = models.CharField(max_length=250)
    data = models.CharField(max_length=250)
    valor = models.CharField(max_length=250)
    metodo = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'pagamentos'