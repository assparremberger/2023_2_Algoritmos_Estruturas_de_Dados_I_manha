from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            #self.fim = nodo
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Fila Vazia!")
        else:
            aux = self.inicio
            texto = ""
            while aux :
                texto += str( aux.dado ) + "  -  "
                aux = aux.proximo
            print( texto )
            print( "Tamanho: ", str(self.tamanho))

    def remover(self):
        if self.inicio == None:
            print("Fila Vazia!")
        else:
            if self.inicio.proximo == None:
                self.fim = None
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            self.imprimir()
            


