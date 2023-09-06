from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao
aluno = Aluno("João", "123456")
aluno.imprimir()
print("---------------")
alunoMedio = AlunoEnsinoMedio("Maria", "123456789", 2 )
alunoMedio.imprimir()
print("---------------")
alunoGrad = AlunoGraduacao("Júlia", "987654", 5 )
alunoGrad.imprimir()