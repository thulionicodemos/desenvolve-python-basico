primeiras_25_linhas = []
print("Texto das primeiras 25 linhas:")

for encoding in ["utf-8", "latin-1"]:
    try:
        with open("estomago.txt", "r", encoding=encoding) as file:
            # Lê as primeiras 25 linhas e exibe
            for i in range(25):
                linha = file.readline().strip()
                primeiras_25_linhas.append(linha)
                print(linha)

            # Retorna ao início do arquivo
            file.seek(0)

            # Número de linhas do arquivo
            num_linhas = sum(1 for _ in file)
            print("\nNúmero de linhas do arquivo:", num_linhas)

            file.seek(0)

            # Linha com maior número de caracteres
            linha_mais_longa = max(file, key=len)
            print("\nLinha com maior número de caracteres:")
            print(linha_mais_longa.strip())

            file.seek(0)

            # Contagem de menções aos nomes dos personagens "Nonato" e "Íria"
            mencoes_nonato = 0
            mencoes_iria = 0
            for linha in file:
                mencoes_nonato += linha.lower().count("nonato".lower())
                mencoes_iria += linha.lower().count("Íria".lower())

            print("\nNúmero de menções a 'Nonato':", mencoes_nonato)
            print("Número de menções a 'Íria':", mencoes_iria)
            break
    except UnicodeDecodeError:
        continue