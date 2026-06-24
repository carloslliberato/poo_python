class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id, titular, saldo=0):
        self.id = id # public +
        self._titular = titular # protected #
        self.__saldo = saldo # private -

    def __str__(self):
        # return f"A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo"
        return f'{self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R${valor:,.2f} na conta {self.id} autorizado.\n')

    def sacar(self, valor):
        valor = abs(valor)
        if valor < self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} da conta {self.id} autorizado.\n')
        else:
            print(f"Saque de R${valor:,.2f} negado. __saldo Insuficiente")
