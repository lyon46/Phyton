#faça um programa que receba um número e imprima sua tabuada
numero = int(input("Digite um número: "))

print("Tabuada de", numero)

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

       # numero = int(input("Digite um número: "))

        #print("Tabuada de", numero)

        #i = 1
        #while i <= 10:
         #   resultado = numero * i
          #  print(numero, "x", i, "=", resultado)
           # i += 1