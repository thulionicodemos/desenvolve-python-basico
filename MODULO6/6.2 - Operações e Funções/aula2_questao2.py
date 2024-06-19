import random

soma, media = 0, 0

# Gera um valor entre 5 e 20 e armazena em num_elementos
num_elementos = random.randint(5, 20)

# Insere valores aleatórios entre 1 e 10 em quantidade correspondente a num_elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Soma os valores da lista ('n' percorre a lista indo do índice 0 ao fim da lista)
for n in elementos:
    soma += n
# Calcula a média dos valores da lista
media = soma/num_elementos

# Exibe a lista elementos
print("Lista:")
print(elementos)

# Exibe a soma dos valores da lista
print("A soma dos valores da lista é: ", soma)

# Exibe a média dos valores da lista
print(f"A média dos valores da lista é: {media:.2f}")