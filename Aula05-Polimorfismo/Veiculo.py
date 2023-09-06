from Categoria import Categoria
class Veiculo:
    def __init__(self, marca, ano=2014, cat = Categoria("Sport")):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.cat = cat
    
    def __str__(self):
        text = "Veículo: " + self.marca + "\n"
        text += "Ano: " + str( self.ano ) + "\n"
        text += "Categoria: " + self.cat.nome + "\n"
        return text

    def imprimir(self):
        print( self )
        #print( self.__str__() )