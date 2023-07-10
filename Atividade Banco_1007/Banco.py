def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def transferir(conta_origem, conta_destino, valor):

    if conta_origem["saldo"] >= valor:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        print("Transferência de R${}".format(valor), "realizada com sucesso!")

    else:
        print("Saldo insuficiente na conta de origem.")


def extrato(conta):
    print("numero: {} \ntitular: {} \nsaldo: {}".format(conta['numero'], conta['titular'], conta['saldo']))

conta1 = cria_conta('123-4', 'Amanda Lopes', 1000.0, 10000.0)
print(conta1['titular'])
conta2 = cria_conta('123-7', 'Olivia Pope', 2000.0, 10000.0)
print(conta2['titular'])

depositar(conta1, 1000.0)
extrato(conta1)

sacar(conta1, 300.0)
extrato(conta1)

transferir(conta2, conta1, 1500.0)
extrato(conta1)