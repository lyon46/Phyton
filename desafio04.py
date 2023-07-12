#escreva um programa que receba uma medida em metros e imprima o valor em centimetros e milimetros
medida = float(input('digite uma medida em metros: '))
centimetros = medida / 100
milimetros = medida / 1000
print('A medida em centímetros é: ', centimetros, 'e em milimetros é:', milimetros)