from Cidade import Cidade
from Pessoa import Pessoa


c1 = Cidade("Viamão", 256302)

p1 = Pessoa("João", 1.70, c1)
#p2 = Pessoa("Maria", 1.75, c1)
#p2 = Pessoa("Maria")
p2 = Pessoa("Maria", city = c1)
p3 = Pessoa("José", 1.6 , c1)

p2.imprimir()
print( "IMC de ", p2.nome, " é: " , p2.getIMC(75) )