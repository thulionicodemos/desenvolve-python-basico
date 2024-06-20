livros = [
    ["A Maldição do Tigre", "Colleen Houck", 2011, 352],
    ["O Resgate do Tigre", "Colleen Houck", 2012, 432],
    ["A Viagem do Tigre", "Colleen Houck", 2012, 560],
    ["O Destino do Tigre", "Colleen Houck", 2013, 464],
    ["A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423],
    ["A Promessa do Tigre", "Colleen Houck", 2014, 256],
    ["As Duas Torres", "J.R.R. Tolkien", 1954, 352],
    ["O Retorno do Rei", "J.R.R. Tolkien", 1955, 416],
    ["O Cavaleiro Preso na Armadura", "Robert Fisher", 1987, 112],
    ["The Hobbit", "J.R.R. Tolkien", 1937, 310]
]

# Cria o arquivo CSV
with open("meus_livros.csv", "w", encoding="latin-1") as file:
    # Escreve o cabeçalho
    file.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escreve as informações dos livros
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        file.write(linha)