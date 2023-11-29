from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, ap):
        if self.inicio == None:
            self.inicio = ap
        else:
            self.fim.proximo = ap
        self.fim = ap
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print( "Fila Vazia ")
        else:
            print( "Fila de espera")
            aux = self.inicio
            texto = ""
            while( aux ):
                texto += str(aux.numero) + ": "
                texto += aux.torre.nome + " - " 
                aux = aux.proximo
            print( texto )
            print( "Total: " , self.tamanho )

    def remover(self, nVaga):
        if self.inicio == None:
            print( "Fila Vazia" )
        else:
            if self.inicio.proximo == None:
                self.fim = None
            self.inicio.vaga = nVaga
            ap = self.inicio
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            self.imprimir()
            ap.proximo = None
            return ap