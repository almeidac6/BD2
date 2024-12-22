# Generated by Django 4.1.13 on 2024-12-22 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
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
