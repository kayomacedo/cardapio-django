import os
from django.db import models

class Sabor(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
def caminho_foto_pizza(instance, filename):
    return os.path.join('assets', filename)

class Pizza(models.Model):
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField('Ingrediente')
    foto = models.ImageField(upload_to=caminho_foto_pizza)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    
    DISPONIVEL = 'DIS'
    ESGOTADO = 'ESG'
    STATUS_CHOICES = [
        (DISPONIVEL, 'Disponível'),
        (ESGOTADO, 'Esgotado'),
    ]
    
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=DISPONIVEL)
    
    def __str__(self):
        return f"{self.sabor} - R${self.preco}"

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
