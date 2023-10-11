from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    # def addNoInicio(self, valor):
    #     no = No(valor)
    #     if self.inicio == None:
    #         self.inicio = no
    #         self.tamanho += 1
    #     else:
    #         no.proximo = self.inicio
    #         self.inicio = no
    #         self.tamanho += 1
    #     # self.imprimir()

    def addNoInicio(self, valor):
        no = No(valor)
        if self.inicio != None:
            no.proximo = self.inicio
        self.inicio = no
        self.tamanho += 1
        self.imprimir()

    def addNoFim(self, valor):
        no = No(valor)
        if self.inicio == None:
            self.inicio = no
        else:
            aux = self.inicio
            while aux.proximo :
                aux = aux.proximo
            aux.proximo = no
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.proximo
            print( "Total: " , self.tamanho)


    # def removerDoInicio(self):
    #     if self.inicio == None:
    #         print("Lista Vazia")
    #     elif self.inicio.proximo == None:
    #         self.inicio = None
    #         self.tamanho = 0
    #     else:
    #         self.inicio = self.inicio.proximo
    #         self.tamanho -= 1
    #     self.imprimir()
    
    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista Vazia")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        self.imprimir()

    def removerDoFim(self):
        if self.inicio == None:
            print("Lista Vazia")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.tamanho = 0
        else:
            anterior = self.inicio
            aux = self.inicio.proximo
            while aux.proximo :
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None
            self.tamanho -= 1
        self.imprimir()