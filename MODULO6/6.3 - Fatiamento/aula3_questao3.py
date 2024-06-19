import random

# Gera lista com 20 números entre -10 e 10
lista = []

for i in range(20):
    lista.append(random.randint(-10, 10))

# Função para encontrar o intervalo com a maior quantidade de números negativos
def encontrar_intervalo_negativos(lista):
    max_negativos = 0
    intervalo_inicial = 0
    intervalo_final = 0

    i = 0
    while i < len(lista):
        if lista[i] < 0:
            inicio = i
            while i < len(lista) and lista[i] < 0:
                i += 1
            fim = i
            negativos = fim - inicio
            if negativos > max_negativos:
                max_negativos = negativos
                intervalo_inicial = inicio
                intervalo_final = fim
        else:
            i += 1

    return intervalo_inicial, intervalo_final

# Encontre o intervalo com a maior quantidade de números negativos
inicio, fim = encontrar_intervalo_negativos(lista)
print(inicio, fim)

print("Lista original:", lista)

# Deleta o intervalo encontrado
del lista[inicio:fim]

print("Lista após a deleção:", lista)