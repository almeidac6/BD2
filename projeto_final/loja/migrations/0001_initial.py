# Generated by Django 4.1.13 on 2024-12-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encomendas',
            fields=[
                ('idencomendas', models.AutoField(primary_key=True, serialize=False)),
                ('idcliente', models.CharField(max_length=250)),
                ('morada', models.CharField(max_length=250)),
                ('datacriacao', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'encomendas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entregas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identregas', models.CharField(max_length=250)),
                ('idpagamentos', models.CharField(max_length=250)),
                ('idfuncionario', models.CharField(max_length=250)),
                ('idveiculo', models.CharField(max_length=250)),
                ('data', models.CharField(max_length=250)),
                ('situacao', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'entregas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpagamentos', models.CharField(max_length=250)),
                ('idencomendas', models.CharField(max_length=250)),
                ('data', models.CharField(max_length=250)),
                ('valor', models.CharField(max_length=250)),
                ('metodo', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'pagamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Armazem',
            fields=[
                ('id_armazem', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('localizacao', models.CharField(max_length=250)),
                ('capacidade', models.IntegerField()),
            ],
            options={
                'db_table': 'armazem',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_funcionario', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
        migrations.CreateModel(
            name='ItemEncomenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encomenda', models.CharField(max_length=250)),
                ('produto', models.CharField(max_length=250)),
                ('quantidade', models.CharField(max_length=250)),
                ('preco', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('id_armazem', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=250)),
                ('preco', models.FloatField()),
                ('descricao', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id_veiculo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=250)),
                ('modelo', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'veiculos',
            },
        ),
    ]
