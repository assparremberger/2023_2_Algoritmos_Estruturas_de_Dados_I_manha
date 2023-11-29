from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila
from Lista import Lista

t1 = Torre("Torre A" , "Rua A, 100" )
t2 = Torre("Torre B" , "Rua B, 200" )

ap1 = Apartamento("101-A" , t1)
ap2 = Apartamento("102-A" , t1)
ap3 = Apartamento("101-B" , t2)
ap4 = Apartamento("103-A" , t1)
ap5 = Apartamento("102-B" , t2)

semVagas = Fila()
apsComVaga = Lista()

semVagas.add( ap1 )
semVagas.add( ap2 )
semVagas.add( ap3 )
semVagas.add( ap4 )
semVagas.add( ap5 )
print(" ------------- --------- ")
ap = semVagas.remover( 1 )
apsComVaga.add( ap )

apsComVaga.add(  semVagas.remover( 2 )  )






