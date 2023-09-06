from Aluno import Aluno
class AlunoEnsinoMedio(Aluno):

    def __init__(self, name, mat, year):
        super().__init__(name, mat)
        self.ano = year

    def imprimir(self):
        print("Aluno Ensino Médio: " , self.nome )
        print("Matrícula:", self.matricula)
        print("Ano:", self.ano)

