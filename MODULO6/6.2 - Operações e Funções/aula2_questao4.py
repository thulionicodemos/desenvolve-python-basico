# Atribuição dos elementos da lista 1
n1 = int(input("Digite a quantidade de elementos da lista 1: "))

lista1 = []
print(f"Digite os {n1} elementos da lista 1: ")
for i in range(n1):
    lista1.append(int(input()))

# Atribuição dos elementos da lista 2
n2 = int(input("Digite a quantidade de elementos da lista 2: "))

lista2 = []
print(f"Digite os {n2} elementos da lista 2: ")
for i in range(n2):
    lista2.append(int(input()))

lista3 = []

# Determina o tamanho máximo entre as duas listas
tamanho = max(len(lista1), len(lista2))

# Combina as listas de forma alternada
for i in range(tamanho):
    if i < len(lista1):
        lista3.append(lista1[i])
    if i < len(lista2):
        lista3.append(lista2[i])

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista intercalada: {lista3}")