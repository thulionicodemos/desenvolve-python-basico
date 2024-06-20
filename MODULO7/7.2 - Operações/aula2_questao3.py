import string

def limpar_frase(frase):
    # Remove espaços e pontuação, e converte para minúsculas
    frase_limpa = ''.join(char for char in frase if char.isalnum()).lower()
    return frase_limpa

def palindromo(frase):
    frase_limpa = limpar_frase(frase)
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input("Digite uma frase (digite fim para encerrar): ")
    
    if frase.lower() == "fim":
        break
    
    if palindromo(frase):
        print(f"'{frase}' é palíndromo")
    else:
        print(f"'{frase}' não é palíndromo")