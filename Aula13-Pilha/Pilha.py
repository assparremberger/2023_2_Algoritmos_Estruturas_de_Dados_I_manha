from Livro import Livro

class Pilha:
    def __init__(self):
        self.top = None
        self.tamanho = 0

    def add(self, livro):
        if self.top != None:
            livro.proximo = self.top
        self.top = livro
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.top == None:
            print("Pilha Vazia")
        else:
            aux = self.top
            while aux :
                print( aux )
                aux = aux.proximo
            print( "Total: " , self.tamanho)

    def remover(self):
        if self.top == None:
            print("Pilha Vazia")
        else: 
            self.top = self.top.proximo
            self.tamanho -= 1
            self.imprimir() 
