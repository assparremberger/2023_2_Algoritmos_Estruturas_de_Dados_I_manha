# método que não recebe parâmetro
# e possui retorno
def getPI():
    return 3.14

def getPIemDobro():
    return getPI() * 2

# método que não recebe parâmetro
# e não possui retorno
def imprimirPI():
    print( getPI() )


# método que recebe parâmetro
# e possui retorno
def getAreaCirculo( raio ):
    a = getPI() * ( raio * raio )
    return a


# método que recebe parâmetro
# e não possui retorno
def imprimirAreaCirculo( r ):
    area = getAreaCirculo( r )
    print("Área com raio " , r , " é de: " , area)


#execução dos métodos
imprimirPI()
imprimirAreaCirculo( 5 )


