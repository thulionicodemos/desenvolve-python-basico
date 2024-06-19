frase = input("Digite uma frase: ")

# Lista de vogais da frase, ordenada alfabeticamente
vogais = [letra.lower() for letra in frase if letra.lower() in 'aeiou']
vogais.sort()

# Lista de consoantes da frase
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']

print("Vogais:", vogais)
print("Consoantes:", consoantes)