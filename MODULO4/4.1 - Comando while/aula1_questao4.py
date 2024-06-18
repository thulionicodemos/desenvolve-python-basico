n = int(input("Digite a quantidade de valores que deseja comparar: "))
maior = 0

while n > 0:
    x = int(input("Digite um número: "))
    
    if x > maior:
        maior = x

    n -= 1

print(f"O maior valor é: {maior}")