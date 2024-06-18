#importar bibliotecas
import math
import random

#solicita a quatidade de valores gerados
n = int(input("Digite a quantidade de valores: "))
soma = 0

#laço de repetição que gera, imprime e soma os valores aleatórios
for i in range(n):
    valor = random.randint(0, 100)
    print(valor)
    soma += valor

#imprime a soma e a raiz da soma
print(soma)
print(f"A raiz quandrada da soma é: {math.sqrt(soma):.2f}")