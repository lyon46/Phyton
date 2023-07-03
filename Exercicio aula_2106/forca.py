import random

palavras = [
    "maçã",
    "banana",
    "laranja",
    "morango",
    "abacaxi",
    "uva",
    "pera",
    "melancia",
    "kiwi",
]


def selecionar_palavra():
    return random.choice(palavras)


def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao


def jogar_forca():
    palavra = selecionar_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        print("\n" + exibir_palavra(palavra, letras_corretas))
        print("Tentativas restantes: ", tentativas)

        if "_" not in exibir_palavra(palavra, letras_corretas):
            print("Parabéns! Você venceu!")
            break

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

        letra = input("Digite uma letra: ")

        if letra in letras_corretas or letra in letras_erradas:
            print(
                "Você já tentou essa letra. Tente novamente!, letras já usadas: "
                + "["
                + ", ".join(list(set((letras_corretas + letras_erradas))))
                + "]"
            )
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            print("Letra incorreta!")


jogar_forca()
