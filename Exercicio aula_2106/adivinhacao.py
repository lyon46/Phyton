import random

numero_secreto = random.randint(0, 100)

dificuldades = {1: 10, 2: 5, 3: 3}

print("Bem Vindo ao Jogo da Adivinhação")
print("Escolha o nível de dificuldade:")
print(" 1 - Fácil \n 2 - Médio \n 3 - Difícil ")
dificuldade_selecionada = int(input())

if dificuldade_selecionada not in dificuldades:
    print("Nível de dificuldade inválido. O jogo será iniciado no nível médio.")
    dificuldade_selecionada = 2

num_tentativas = dificuldades[dificuldade_selecionada]

pontuacao = 1000

while num_tentativas > 0:
    print("Tente adivinhar o número secreto (entre 0 e 100):")
    chute = int(input())

    diferenca = abs(chute - numero_secreto)

    pontuacao -= diferenca

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        break
    elif chute > numero_secreto:
        print("Errou, chute alto!")
    else:
        print("Errou, chute baixo!")

    num_tentativas -= 1

    print("Pontuação atual:", pontuacao)
    print("Tentativas restantes:", num_tentativas)

if num_tentativas == 0:
    print("Fim do jogo! Sua pontuação chegou a 0!")
    print("O número secreto era:", numero_secreto)
    print("Pontuação final:", pontuacao)
