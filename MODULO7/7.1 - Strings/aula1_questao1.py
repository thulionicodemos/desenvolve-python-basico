nome = str(input("Digite seu nome: "))

for i in range(len(nome)+1):
    # Imprime a substring do início até o índice i
    print(nome[:i])