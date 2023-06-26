import random
import time

def exibir_personagem():
    print('''
         O
        \|/
         |
        / \\
    ''')

def jogar_adivinhacao():
    palavras = ['biomob', 'petropolis', 'serratec', 'filipe', 'internet', 'cerveja']
    palavra_secreta = random.choice(palavras).lower()
    palavra_adivinhada = ['_'] * len(palavra_secreta)
    tentativas = 6
    letras_usadas = []

    print("Bem-vindo ao jogo de adivinhação de palavras!")
    time.sleep(1)
    print("Estou pensando em uma palavra...")
    time.sleep(1)
    print("Tente adivinhar qual é preenchendo as letras uma por uma.")
    time.sleep(1)
    print("Vamos começar!")

    while True:
        exibir_personagem()
        print(' '.join(palavra_adivinhada))
        print("Tentativas restantes:", tentativas)
        print("Letras usadas:", ', '.join(letras_usadas))

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_usadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_usadas.append(letra)

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    palavra_adivinhada[i] = letra

            if '_' not in palavra_adivinhada:
                print(' '.join(palavra_adivinhada))
                print("Parabéns! Você acertou a palavra!")
                break
        else:
            tentativas -= 1
            print("Letra incorreta!")

            if tentativas == 0:
                exibir_personagem()
                print("Você perdeu! A palavra secreta era:", palavra_secreta)
                break

        print()

    print("Obrigado por jogar!")

jogar_adivinhacao()
