from Categoria import Categoria
class Produto:

    def __init__(self, nome, preco = 0.0 , cat = Categoria("Diversos") ):
        self.nome = nome
        self.preco = preco
        self.cat = cat

    def __str__(self):
        texto = "Produto: " + self.nome + "\n"
        texto += "Preço: " + str(self.preco) + "\n"
        texto += str( self.cat )
        return texto
        
    def imprimir(self):
        print( self.__str__() )

