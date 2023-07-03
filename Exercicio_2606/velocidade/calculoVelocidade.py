from divisao import divisao


def calculaVelocidade(tempo, espaco):
    velocidade = divisao(tempo, espaco)
    return velocidade


tempo = float(input("Digite o valor do tempo: "))
espaco = float(input("Digite o valor do espaço: "))

velocidade = calculaVelocidade(tempo, espaco)

print("Valor do tempo:", tempo)
print("Valor do espaço:", espaco)
print("Resultado da velocidade:", velocidade)
