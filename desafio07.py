#crie um programa que leia a largura e altura de uma parede em metros,
# calcule sua area e a quantidade de tinta necessária para pintá-la, sabendo que
#cada litro de tinta, pinta uma área de 2m²

altura = float(input('Digite a altura: '))
largura = float(input('Agora digite a largura:'))
litro = 2
area: float  = (altura * largura) / litro
print('Você vai precisar de: ', area , 'litros de tinta')