from Veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def ligar(self):
        print("Coloque o capacete!")

    def imprimir(self):
        super().imprimir()
        print("Cilindradas: " , str(self.cilindradas) )
