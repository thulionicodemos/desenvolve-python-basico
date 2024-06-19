import random

# Gerar os valores
valores = [random.randint(-100, 100) for _ in range(20)]

# Ordena a lista
valores_ordenados = sorted(valores)

# Encontra o índice do maior e menor valor
indice_maior_valor = valores.index(max(valores))
indice_menor_valor = valores.index(min(valores))

# Exibe a lista ordenada
print("Lista ordenada (sem modificar a original):")
print(valores_ordenados)

# Exibe a lista original
print("Lista original:")
print(valores)

# Exibe o índice do maior valor
print("Índice do maior valor da lista: ", indice_maior_valor)

# Exibe o índice do menor valor
print("Índice do menor valor da lista: ", indice_menor_valor)