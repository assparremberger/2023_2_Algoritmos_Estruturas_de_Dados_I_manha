from Aluno import Aluno
class AlunoGraduacao(Aluno):

    def __init__(self, name, mat, semestre):
        super().__init__(name, mat)
        self.semestre = semestre

    def imprimir(self):
        print("Aluno Graduação: " , self.nome )
        print("Matrícula:", self.matricula)
        print("Semestre:", self.semestre)

