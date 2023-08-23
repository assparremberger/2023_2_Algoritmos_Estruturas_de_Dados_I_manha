from Cidade import Cidade
class Pessoa:

#    def __init__(self, nome, altura = 1.75 , city = Cidade(None, None)):
#    def __init__(self, nome, altura = 1.75 , city = Cidade("Porto Alegre", 1500000)):
    def __init__(self, nome, altura = 1.75 , city = Cidade() ):
        self.nome = nome
        self.altura = altura
        self.cidade = city

    def __str__(self):
        texto = "Nome: " + self.nome + "\n"
        texto += "Altura: " + str(self.altura) + "\n"
    #    texto += "Cidade: " + self.cidade.__str__()
        texto += str( self.cidade )
        return texto

    def getIMC(self, peso):
        imc = peso / (self.altura * self.altura )
        return imc
    
    def imprimir(self):
        print( self.__str__() )

