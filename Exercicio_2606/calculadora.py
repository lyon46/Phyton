def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

resultado_adicao = adicao(a, b)
print("Resultado da adição:", resultado_adicao)

resultado_subtracao = subtracao(a, b)
print("Resultado da subtração:", resultado_subtracao)

resultado_multiplicacao = multiplicacao(a, b)
print("Resultado da multiplicação:", resultado_multiplicacao)

resultado_divisao = divisao(a, b)
print("Resultado da divisao:", resultado_divisao)
