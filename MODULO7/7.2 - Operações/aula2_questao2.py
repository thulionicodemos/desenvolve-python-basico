frase = str(input("Digite uma frase: "))

# Deixa a frase em minúsculo e substitui as vogais por '*'
frase = frase.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')

print(frase)