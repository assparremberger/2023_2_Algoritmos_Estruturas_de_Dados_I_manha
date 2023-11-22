f1 = { "nome": "Júlia" , "idade" : 15 }
f2 = { "nome": "Junior" , "idade" : 10 }
f3 = { "nome": "Hamilton" , "idade" : 2 }

print( f1 )

for chave, valor in f1.items():
    print( chave , " - ", valor)
print(" ------------------ ")
for chave in f1.keys():
    print( chave , " - ", f1[chave])

print(" \n\n ------Tupla de Dicionários ------------")
filhos = f1 , f2
print( filhos )
#filhos[1] = f3
f2["nome"] = "José"
print( filhos )