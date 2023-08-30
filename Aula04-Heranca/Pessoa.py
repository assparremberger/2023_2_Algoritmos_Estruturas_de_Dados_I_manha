class Pessoa:
    def __init__(self, name, phone):
        self.nome = name 
        self.fone = phone
    def __str__(self):
        text = "Pessoa: " + self.nome + "\n"
        text += "Fone: " + self.fone + "\n"
        return text
    def imprimir(self):
        print( self )