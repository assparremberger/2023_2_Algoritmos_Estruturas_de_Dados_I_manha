from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, modelo, ano, nPortas):
        super().__init__(modelo, ano)
        self.nPortas = nPortas

    def ligar(self):
        print("Coloque o cinto de segurança!")

    def imprimir(self):
        super().imprimir()
        print("Portas: " , str(self.nPortas) )
