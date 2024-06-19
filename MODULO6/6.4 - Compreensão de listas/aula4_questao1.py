# Lista de todos os números pares entre 20 e 50
pares = [num for num in range(20, 51) if num % 2 == 0]

# Lista dos quadrados de todos os valores de 1 a 9
quadrados = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Lista de todos os números entre 1 e 100 que são divisíveis por 7
divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]

# Lista indicando "par" ou "ímpar" para valores em range(0,30,3)
par_ou_impar = ['par' if num % 2 == 0 else 'ímpar' for num in range(0, 30, 3)]

print("Números pares entre 20 e 50:", pares)
print("Quadrados de 1 a 9:", quadrados)
print("Números divisíveis por 7 de 1 a 100:", divisiveis_por_7)
print("Par ou ímpar para valores de range(0, 30, 3):", par_ou_impar)