import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        # Não embaralha a palavra se mesma tem menos que 3 caracteres
        if len(palavra) <= 3:
            return palavra
        # Mantém a primeira e a última letra no lugar
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    
    # Divide a frase em palavras
    palavras = frase.split()
    # Embaralha cada palavra usando a função 'embaralhar_palavra'
    palavras_embaralhadas = [embaralhar_palavra(i) for i in palavras]
    # Recombina as palavras embaralhadas em uma frase
    frase_embaralhada = ' '.join(palavras_embaralhadas)
    
    return frase_embaralhada

# Saída
frase = input("Digite uma frase: ")
print(embaralhar_palavras(frase))