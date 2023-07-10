def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite, "historico": []}
    return conta


def transferir(conta_origem, conta_destino, valor):
    if conta_origem["saldo"] >= valor:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        transacao(conta_origem, "Transferência enviada para a conta {}".format(conta_destino['numero']), -valor)
        transacao(conta_destino, "Transferência recebida da conta {}".format(conta_origem['numero']), valor)
        print("Transferência de R${}".format(valor), "realizada com sucesso!")
    else:
        print("Saldo insuficiente na conta de origem.")

def sacar(conta, valor):
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        transacao(conta, "Saque", -valor)
        print("Saque de R${}".format(valor), "realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

def depositar(conta, valor):
    conta["saldo"] += valor
    transacao(conta, "Depósito", valor)
    print("Depósito de R${}".format(valor), "realizado com sucesso!")

def transacao(conta, tipo, valor):
    transacao = {"tipo": tipo, "valor": valor}
    conta["historico"].append(transacao)

def extrato(conta):
    print("Número da conta: {}".format(conta['numero']))
    print("Titular da conta: {}".format(conta['titular']))
    print("Saldo da conta: R${}".format(conta['saldo']))
    print("Limite da conta: R${}".format(conta['limite']))
    print("-----------------------")

def historico(conta):
    print(f"Histórico da conta {conta['numero']} - {conta['titular']}:")
    for transacao in conta["historico"]:
        tipo = transacao["tipo"]
        valor = transacao["valor"]
        print(f"Tipo: {tipo}, Valor: {valor}")
    print("-----------------------")



conta1 = cria_conta('0649-0', 'Heloisa Oliveira', 1000.0, 10000.0)

conta2 = cria_conta('0532-1', 'Gustavo Bueno', 2000.0, 15000.0)

conta3 = cria_conta('1380-5', 'Maicon Bueno', 3000.0, 17000.0)

transferir(conta1, conta2, 200)

depositar(conta1, 1200.0)

depositar(conta2, 450.0)

depositar(conta3, 150.0)

transferir(conta3, conta1, 680.0)


sacar(conta1, 340.0)

sacar(conta3, 750.0)

transferir(conta2, conta3, 780.0)

sacar(conta2, 50)

print("Extrato da conta 1:")
extrato(conta1)

print("Extrato da conta 2:")
extrato(conta2)

print("Extrato da conta 3:")
extrato(conta3)

print("Histórico da conta 1:")
historico(conta1)

print("Histórico da conta 3:")
historico(conta3)