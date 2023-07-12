#Leia 3 números de ponto flutuante. Depois, imprima as raízes da
# fórmula de bhaskara. Caso seja impossível calcular as raízes devido
# a uma divisão por zero ou raiz quadrada de um número negativo,
# apresenta a mensagem “Impossível calcular” .

#Entrada
#Leia 3 números de ponto flutuante (duplo) A, B e C.

#Saída
#Imprima o resultado com 5 dígitos após a vírgula ou a mensagem caso seja impossível calcular.

import math

a, b, c = [float(x) for x in input().strip().split(' ')]

delta = b * b - 4 * a * c

if(a != 0 and delta > -1):
    R1 = (- b + math.sqrt(delta))/(2 * a)
    R2 = (- b - math.sqrt(delta))/(2 * a)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")