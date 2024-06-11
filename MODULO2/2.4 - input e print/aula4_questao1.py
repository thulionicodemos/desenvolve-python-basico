#Recebe o comprimento do terreno como um inteiro
comprimento = int(input("Digite o coomprimento do terreno em metros"))

#Recebe a largura do terreno como um inteiro
largura = int(input("Agora digite a largura do terreno em metros"))

#Recebe o valor do metro quadrado em ponto flutuante
precoM2 = float(input("Por fim, entre com preço do metro quadrado em reais"))

#Imprime a área e preço do terreno
print("O terreno possui ", comprimento*largura, "m2 e custa R$", comprimento*largura*precoM2)