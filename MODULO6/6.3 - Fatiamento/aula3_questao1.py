# Solicita ao usuário pelo menos 4 números inteiros
n = []
while len(n) < 4:
    num = input("Digite um número inteiro (ou pressione Enter para finalizar): ")
    if num == "":
        print("É necessário inserir pelo menos 4 números inteiros.")
        continue
    if not num.isdigit():
        print("Por favor, digite um número inteiro válido.")
        continue
    n.append(int(num))

# Solicita números até o usuário decidir parar
while True:
    num = input("Digite mais um número inteiro (ou pressione Enter para finalizar): ")
    if num == "":
        break
    if not num.isdigit():
        print("Por favor, digite um número inteiro válido.")
        continue
    n.append(int(num))

print("Lista original:", n)

print("Os 3 primeiros elementos:", n[:3])

print("Os 2 últimos elementos:", n[-2:])

print("A lista invertida:", n[::-1])

print("Elementos de índice par:", n[::2])

print("Elementos de índice ímpar:", n[1::2])