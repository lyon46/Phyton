def desenhar_forca(tentativas):
    forca = [
        '''
           +---+
               |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        '''
    ]
    return forca[tentativas]


def jogar_forca(palavra_secreta):
    letras_erradas = []
    letras_corretas = []
    tentativas = 5

    while True:
        for letra in palavra_secreta:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        print('\n')
        print(desenhar_forca(tentativas))
        print("Letras erradas:", letras_erradas)

        letra_palpite = input("Digite uma letra: ").lower()

        if letra_palpite in palavra_secreta:
            letras_corretas.append(letra_palpite)

            if len(letras_corretas) == len(set(palavra_secreta)):
                print("Parabéns! Você venceu!")
                break
        else:
            letras_erradas.append(letra_palpite)
            tentativas += 1

            if tentativas == len(desenhar_forca(0)) - 1:
                print(desenhar_forca(tentativas))
                print("Game Over! A palavra secreta era:", palavra_secreta)
                break

        print('\n')


def main():
    palavra_secreta = input("Digite a palavra secreta: ").lower()
    print("Iniciando o jogo da forca!")
    jogar_forca(palavra_secreta)


if __name__ == '__main__':
    main()
