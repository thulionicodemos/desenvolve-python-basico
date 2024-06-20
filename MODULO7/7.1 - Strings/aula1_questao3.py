frase = str(input("Digite uma frase: "))
cont_espacos = 0

for i in range(len(frase)):
    if frase[i] == " ":
        cont_espacos += 1

print(f"Espaços em branco: {cont_espacos}")