from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nomeF, telefone, cpf):
        super().__init__( nomeF , telefone )
        self.cpf = cpf

