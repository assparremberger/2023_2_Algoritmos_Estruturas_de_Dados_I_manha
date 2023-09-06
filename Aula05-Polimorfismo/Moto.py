from Veiculo import Veiculo

class Moto( Veiculo ):

    def __init__(self, marca, ano, cat, cilin):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilin 

    def __str__(self):
        text = "Motocicleta: " + self.marca + "\n"
        text += "Ano: " + str( self.ano ) + "\n"
        text += "Categoria: " + self.cat.nome + "\n"
        text += "Cilindradas: " + str( self.cilindradas ) +"\n"
        return text

    def imprimir(self):
        print( self )

    # str do Carro
    # def __str__(self):
    #     text = super().__str__()
    #     text += "Portas: " + str( self.qtdPortas ) +"\n"
    #     return text


    
