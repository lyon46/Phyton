import math


def calculadora_inteligente():
    print("Bem-vindo à Calculadora Inteligente!")

    while True:
        print("\nEscolha uma operação:")
        print("1 - Cálculo")
        print("2 - Raiz Quadrada")
        print("3 - Porcentagem")
        print("0 - Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "0":
            print("Calculadora encerrada. Até logo!")
            break

        if escolha == "1":
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))

            resultado = calcular(num1, operador, num2)
            print("Resultado:", resultado)

        elif escolha == "2":
            num = float(input("Digite o número: "))
            resultado = raiz_quadrada(num)
            print("Raiz Quadrada:", resultado)

        elif escolha == "3":
            num = float(input("Digite o número: "))
            percentual = float(input("Digite o percentual (%): "))
            resultado = calcular_porcentagem(num, percentual)
            print("{}% de {} é igual a {}".format(percentual, num, resultado))

        else:
            print("Opção inválida. Por favor, escolha novamente.")


def calcular(num1, operador, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        return "Operador inválido"


def raiz_quadrada(num):
    return math.sqrt(num)


def calcular_porcentagem(num, percentual):
    return (percentual / 100) * num



calculadora_inteligente()

