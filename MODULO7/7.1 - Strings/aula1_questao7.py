import random

def encrypt(nomes):
    nomes_criptografados = []
    n = random.randint(1, 10)
    
    # Função para criptografar um único caractere
    def criptografar_caractere(c, n):
        novo_char_code = ord(c) + n
        if novo_char_code > 126:
            novo_char_code = 33 + (novo_char_code - 127)
        return chr(novo_char_code)
    
    # Criptografar cada nome na lista
    for i in nomes:
        nome_criptografado = ''.join(criptografar_caractere(c, n) for c in i)
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"Nomes: {nomes}")
print(f"Chave Aleatória: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")