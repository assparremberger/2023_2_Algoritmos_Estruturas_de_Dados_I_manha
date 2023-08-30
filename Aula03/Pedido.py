from Produto import Produto
from Pessoa import Pessoa

class Pedido:

    def __init__(self, endereco, cli ):
        self.end = endereco
        self.cliente = cli
        self.produtos = []

    def addProduto(self, prod):
        self.produtos.append( prod )
        total = 0.0
        for product in self.produtos:
            total += product.preco
        return total

    def __str__(self):
        text = "Endereço do Pedido: " + self.end +"\n"
        text += "Cliente: " + self.cliente.nome + "\n"
        text += "Produtos: \n"
        if len( self.produtos ) == 0:
            text += "Pedido Vazio!"
        else:
            for product in self.produtos:
                text += str( product ) + "\n ---------\n"
        return text
                