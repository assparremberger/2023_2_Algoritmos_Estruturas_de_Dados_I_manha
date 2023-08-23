class Categoria:

    def __init__(self, nome = None, id = None):
        self.id = id
        self.nome = nome
        
    def __str__(self):
        return "Categoria: " + self.nome + "\n" 

    def imprimir(self):
        print( self.__str__() )