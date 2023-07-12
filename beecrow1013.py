#Faça um programa que leia 3 valores inteiros e apresente
# o maior seguido da mensagem "eh o maior".


maior = lambda a, b: (a + b + abs(a - b))//2

a, b, c = [int(x) for x in input().split(' ')]

resposta = maior(a, maior(b, c))

print(f"{resposta} eh o maior")