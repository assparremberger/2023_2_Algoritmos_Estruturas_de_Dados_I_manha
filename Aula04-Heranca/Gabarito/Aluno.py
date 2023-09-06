class Aluno:

    def __init__(self, nome, matricula):
        self.codigo = None
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Aluno: " , self.nome )
        print("Matrícula:", self.matricula)
