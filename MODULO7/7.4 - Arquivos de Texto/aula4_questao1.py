from pathlib import Path

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Obtém o caminho completo do arquivo
caminho_arquivo = Path(__file__).parent / nome_arquivo

# Salva a frase no arquivo
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {caminho_arquivo}")