class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente para saque.")

    def transferir(self, outra_conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            outra_conta.depositar(valor)
            print(f"Transferência de {valor} realizada.")
        else:
            print("Saldo insuficiente para transferência.")

    def verificar_saldo(self):
        print(f"Saldo atual: {self.saldo}")



conta1 = ContaBancaria(100)
conta2 = ContaBancaria(50)

conta1.verificar_saldo()
conta2.verificar_saldo()

conta1.transferir(conta2, 30)
conta1.verificar_saldo()
conta2.verificar_saldo()

conta2.sacar(100)

conta1.transferir(conta2, 50)
conta1.verificar_saldo()
conta2.verificar_saldo()