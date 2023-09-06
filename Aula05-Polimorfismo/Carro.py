from Veiculo import Veiculo

class Carro( Veiculo ):

    def __init__(self, marca, ano, cat, portas):
        super().__init__(marca, ano, cat)
        self.qtdPortas = portas 

    def __str__(self):
        text = super().__str__()
        text += "Portas: " + str( self.qtdPortas ) +"\n"
        return text
        #return super().__str__() + "Portas: " + str( self.qtdPortas ) +"\n"
 
#    def imprimir(self):
#        super().imprimir()
#        print( "Portas: " + str( self.qtdPortas ) +"\n" )

    def imprimir(self):
        print( self )
