#O Joãozinho quer calcular e mostrar a quantidade de litros de combustível
# gastos em uma viagem, usando um carro que faz 12 Km/L. Para isso, ele gostaria que
# você o ajudasse por meio de um programa simples. Para realizar o cálculo, você deve ler
# o tempo gasto (em horas) e a mesma velocidade média (km/h). Dessa forma, você pode obter
# a distância e, a seguir, calcular quantos litros seriam necessários.
# Mostre o valor com três casas decimais após o ponto.

#Entrada
#O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas).
# A segunda é a velocidade média durante a viagem (em Km/h).

#Saída
#Imprima quantos litros seriam necessários para fazer esta viagem, com três dígitos após a vírgula.


tempo = int(input('digite o tempo:'))
velocidade = int(input('digite a velocidade:'))

distancia = tempo * velocidade
litros = distancia/12

print(f"{litros:.3f}")