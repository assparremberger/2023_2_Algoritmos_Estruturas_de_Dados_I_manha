class Conta:

    tarifa = 1.99
    logado = True

    def __init__(self):
        self.__saldo = 0.0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            print("Deve estar logado para acessa-lo!")
            return None

    def setSaldo(self, valor):
        if self.logado and valor >= 0.0:
            self.__saldo = valor
        else:
            print("Deve estar logado e o valor ser maior que Zero!")

    @property
    def saldo(self):
        if self.logado:
            return self.__saldo
        else:
            print("Deve estar logado para acessa-lo!")
            return None

    @saldo.setter
    def saldo(self, valor):
        if self.logado and valor >= 0.0:
            self.__saldo = valor
        else:
            print("Deve estar logado e o valor ser maior que Zero!")
    
    def __descontarTarifa(self):
        self.__saldo -= self.tarifa

    def depositar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo += valor
            self.__descontarTarifa()
        else:
            print("Valor insuficiente")

    def sacar(self, valor):
        if self.__saldo - valor >= self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa()
        else:
            print("Saldo insuficiente")
