class Torre:

    def __init__(self, nome, end):
        self.id = None
        self.nome = nome
        self.endereco = end

    def cadastrar(self):
        print("Torre cadastrada!")

    def __str__(self):
        text = "Nome: " + self.nome
        text += "\nEndereço: " +  self.endereco
        return text

    def imprimir(self):
        print( self )

    