n = str(input("Digite o número: "))
nDig = "9"
if len(n) == 8:
    print(f"Número completo: {nDig+n[:4]}-{n[4:8]}")
elif len(n)==9:
    print(f"Número completo: {n[:5]}-{n[5:9]}")
else:
    print("Número inválido!")