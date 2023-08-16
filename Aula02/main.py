from Pessoa import Pessoa

p1 = Pessoa( idade=25, name="Maria")
# p2 = Pessoa( idade=25, name="Maria")
print( "Nome: ", p1.nome)
print("------------")
p2 = p1
print( p1 )
print( p2 )