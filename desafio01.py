#crie um programa que recebe um numero e imprima o sucessor e o antecessor

n1 = int(input('digite um número: '))
n2 = n1 - 1
n3 = n1 + 1
print('O sucessor é: ', n3, 'E o antecessor é: ', n2)
#outra maneira de fazer é:
# n = int(input('digite um numero')) print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {} .format(n, (n-1), (n+1)))