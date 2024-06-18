d = float(input("Digite a distância da entrega (em Km): "))
peso = float(input("Digite o peso do pacote (em Kg): "))
frete = 0

if peso > 10:
    frete += 10

if d >= 0 and d <= 100:
    frete = frete + peso
    print(f"O valor do frete é R${frete:.2f}")
elif d > 100 and d <= 300:
    frete = frete + peso * 1.5
    print(f"O valor do frete é R${frete:.2f}")
elif d > 300:
    frete = frete + peso * 2
    print(f"O valor do frete é R${frete:.2f}")