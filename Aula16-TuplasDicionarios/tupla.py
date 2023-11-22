carros = "Uno", "Doblo", "Toro", "Jeep", "Hylux"

print( carros[1] )
print( carros[1:3] )
print( carros[1:] )
print( carros[1:-2] )

itens = carros[3:] , carros[0] , 2
print( itens )

#carros[0] = "Novo Uno"
#print( carros )

def calcular( x , y):
    return x+y , x-y , x*y , x/4

resultado = calcular( 10 , 2 )
print("Result: " , resultado )
print( "Soma:" , resultado[0])

a , b , c , d = calcular( 9 , 3 )
print( "Soma: ", a)
print( "Subtração: ", b)
print( "Multiplicação: ", c)
print( "Divisão: ", d)