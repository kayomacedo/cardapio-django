# Generated by Django 5.0.2 on 2024-02-10 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='pizzas/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('DIS', 'Disponível'), ('ESG', 'Esgotado')], default='DIS', max_length=3)),
                ('ingredientes', models.ManyToManyField(to='cardapio.ingrediente')),
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardapio.sabor')),
            ],
        ),
    ]
