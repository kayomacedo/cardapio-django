
from django.shortcuts import render
from django.http import HttpResponse

from .models import Pizza

class CarrinhoCompra:
    def __init__(self):
        self.lista = []


    def addItem(self,item):
        try:

            self.lista.append(item)
        except:
            return "Error"
    
    def getItens(self):

        return self.lista
    
    def removerItem(self,item):
        try:
            self.lista.remove(item)
        except:
            return "Error"




def home(request):
    carrinho = CarrinhoCompra()

    print(carrinho.getItens())
    pizzas = Pizza.objects.all()
    
    # Verifica se a solicitação é um POST
    if request.method == 'POST':
        print('A solicitação foi feita por meio de POST')
        # Se for necessário realizar alguma ação específica para POST, você pode fazer isso aqui
        carrinho.addItem('item')
    
    # Verifica se a solicitação é um GET
    elif request.method == 'GET':
        print('A solicitação foi feita por meio de GET')
        # Se for necessário realizar alguma ação específica para GET, você pode fazer isso aqui
    
    # Se a solicitação não for nem POST nem GET, não será feito nenhum print
    
    return render(request, 'home.html', {'pizzas': pizzas})
