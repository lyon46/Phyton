def encontraMaior(lista):
    return max(lista)


def encontraMenor(lista):
    return min(lista)


def retornaPares(lista):
    return [num for num in lista if num % 2 == 0]


def contaOcorrenciasPrimeiroElemento(lista):
    primeiro_elemento = lista[0]
    return lista.count(primeiro_elemento)


def calculaMedia(lista):
    return sum(lista) / len(lista)


def somaNegativos(lista):
    soma = 0
    for num in lista:
        if num < 0:
            soma += num

    return soma


lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

# Imprimir o maior elemento
maior_elemento = encontraMaior(lista)
print("Maior elemento:", maior_elemento)

# Imprimir o menor elemento
menor_elemento = encontraMenor(lista)
print("Menor elemento:", menor_elemento)

# Imprimir os números pares
numeros_pares = retornaPares(lista)
print("Números pares:", numeros_pares)

# Imprimir o número de ocorrências do primeiro elemento da lista
ocorrencias = contaOcorrenciasPrimeiroElemento(lista)
print("Número de ocorrências do primeiro elemento:", ocorrencias)

# Imprimir a média dos elementos
media = calculaMedia(lista)
print("Média dos elementos:", media)

# Imprimir a soma dos elementos de valor negativo
soma_negativos = somaNegativos(lista)
print("Soma dos elementos de valor negativo:", soma_negativos)
