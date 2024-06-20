def encontrar_anagramas(frase, palavra_objetivo):
    anagramas = []
    
    # Ordenar os caracteres da string e converter para minúsculo
    def ordenar_palavra(palavra):
        return ''.join(sorted(palavra.lower())) # .join concatena caracteres da string
    
    palavra_objetivo_ordenada = ordenar_palavra(palavra_objetivo)
    
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Verifica cada palavra na frase
    for i in palavras:
        # Remover pontuações e tornar a string minúscula
        palavra_limpa = ''.join(filter(str.isalpha, i)).lower()
        
        if ordenar_palavra(palavra_limpa) == palavra_objetivo_ordenada:
            anagramas.append(i)
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = encontrar_anagramas(frase, palavra_objetivo)

print(f"Anagramas: {anagramas}")