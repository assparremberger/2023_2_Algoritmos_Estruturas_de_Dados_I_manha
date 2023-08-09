carros = ["Bugatti", "Uno", "Doblo", "Renegade"]
print(carros)
print("Meu primeiro carro: " , carros[1] )
print( carros[1:3])
print( carros[-3:-1])

for i in range( len(carros) ):
    print( "Posição: ", i , ": " + carros[i])

print("------------------ ")
cont = 0
for car in carros:
    print( "Posição: ", cont , ": " + car)
    cont += 1
