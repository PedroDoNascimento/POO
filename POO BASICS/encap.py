class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, quantia):
        self.__saldo += quantia

    def sacar(self, quantia):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
        else:
            print('Saldo insuficiente')

    def mostrar_saldo(self):
        print(f'Saldo: {self.__saldo}')

conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(300)
conta.mostrar_saldo()  # Output: Saldo: 1200