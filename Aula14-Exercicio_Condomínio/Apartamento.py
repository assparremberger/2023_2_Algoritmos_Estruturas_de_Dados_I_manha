from Torre import Torre

class Apartamento:

    def __init__(self, numero, torre):
        self.id = None
        self.numero = numero
        self.torre = torre
        self.vaga = None
        self.proximo = None

    def cadastrar(self):
        print("Apartamento cadastrado!")

    def __str__(self):
        text = "Número: " + str( self.numero ) 
        text += "\nVaga: " + str( self.vaga ) 
        text += "\nTorre: " + self.torre.nome 
        return text

    def imprimir(self):
        print( self )
