from pathlib import Path
import re

# Define o nome dos arquivos
nome_arquivo_frase = "frase.txt"
nome_arquivo_palavras = "palavras.txt"

# Obtém o caminho completo dos arquivos
caminho_arquivo_frase = Path(__file__).parent / nome_arquivo_frase
caminho_arquivo_palavras = Path(__file__).parent / nome_arquivo_palavras

# Lê o conteúdo do arquivo frase.txt
with open(caminho_arquivo_frase, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos e separa as palavras
palavras = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', conteudo)

# Salva cada palavra em uma nova linha no arquivo palavras.txt
with open(caminho_arquivo_palavras, "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

# Lê e imprime o conteúdo do arquivo palavras.txt
with open(caminho_arquivo_palavras, "r", encoding="utf-8") as arquivo:
    conteudo_palavras = arquivo.read()

print(conteudo_palavras)