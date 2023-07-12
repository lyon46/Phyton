#crie um programa que receba um valor e imprima quantos litros de gasolina ela vai poder colocar no carro
valor = float(input('qual é o valor que você tem? '))
gasolina = float(input('qual é o valor da gasolina atual? '))
total = valor / gasolina
print('A quantidade de litros é: ' ,total)