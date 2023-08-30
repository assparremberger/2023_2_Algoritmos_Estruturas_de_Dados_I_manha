from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nomeJ, telefone, cnpj):
        super().__init__( nomeJ , telefone )
        self.cnpj = cnpj