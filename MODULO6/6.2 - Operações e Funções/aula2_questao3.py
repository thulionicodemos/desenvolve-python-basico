import random

# Gerar os valores para as listas
lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

interseccao = []

for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)
# Saídas
print("Lista 1: ", lista1)

print("Lista 2: ", lista2)

print("Lista Intersecção: ", sorted(interseccao))

# Exibe a quantidade de vezes que cada elemento aparece em cada lista
print("Contagem:")
for i in interseccao:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")