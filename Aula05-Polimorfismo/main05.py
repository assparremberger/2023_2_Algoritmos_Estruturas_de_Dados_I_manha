from Categoria import Categoria
from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

cat01 = Categoria("SUV")
cat02 = Categoria("Sedan")
cat03 = Categoria("Estradeira")

v1 = Veiculo("Fiat")

car01 = Carro("Jeep", 2021, cat01, 4)
car02 = Carro("Fiat", 2020, cat01, 2)

mt01 = Moto("Honda", 2023, cat03, 300)

v1.imprimir()
print("------------")
car01.imprimir()
print("------------")
mt01.imprimir()

