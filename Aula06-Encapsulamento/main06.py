from Conta import Conta

print("Tarifa: " , Conta.tarifa)

c = Conta()
c.__saldo = 100
print("Saldo: " , c.__saldo)
print("Saldo: " , c.getSaldo() )

c.depositar( 100 )
print("Saldo: " , c.saldo )
c.sacar( 50 )
print("Saldo: " , c.saldo )

c.saldo = 300
print("Saldo: " , c.saldo )