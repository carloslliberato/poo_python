class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id, titular, saldo=0):
        self.id = id
        self.titular = titular 
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} na conta {self.id} autorizado.\n')

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} da conta {self.id} autorizado.\n')
        else:
            print(f"Saque de R${valor:,.2f} negado. Saldo Insuficiente")


# Não é recomendado uso de print dentro de classes, uso para melhor entendimento

c1 = ContaBancaria(112, 'Carlos', 3000)
c1.depositar(500)
print(c1)
c1.sacar(1000)
c1.sacar(2_000_000)
print(c1)
print(c1.__doc__)