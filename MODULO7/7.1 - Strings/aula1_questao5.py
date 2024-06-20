frase = str(input("Digite uma frase: "))
cont_vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiou":
        cont_vogais += 1
        indices.append(i)

print(f"{cont_vogais} vogais")
print(f"Indices: {indices}")