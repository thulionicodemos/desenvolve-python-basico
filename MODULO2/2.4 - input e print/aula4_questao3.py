#Dados do produto 1
p1 = input("Digite o nome do produto 1: ")
precop1 = float(input("Digite o preço unitário do produto 1: "))
quantp1 = int(input("Digite a quantidade do produto 1: "))

#Dados do produto 2
p2 = input("Digite o nome do produto 2: ")
precop2 = float(input("Digite o preço unitário do produto 2: "))
quantp2 = int(input("Digite a quantidade do produto 2: "))

#Dados do produto 3
p3 = input("Digite o nome do produto 3: ")
precop3 = float(input("Digite o preço unitário do produto 3: "))
quantp3 = int(input("Digite a quantidade do produto 3: "))

#Calcula o valor total
total = precop1*quantp1 + precop2*quantp2 + precop3*quantp3

#Imprime o valor total com duasa casas decimais
print(f"Total: R${total:.2f}")