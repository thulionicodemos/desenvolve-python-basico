#Recebe a temperatura em graus F
f = float(input("Entre com a temperatura em  °F"))

#Converte a temperatura em graus C e muda o tipo da variável para int
c = (f-32) * (5/9)
c = int(c)

#Imprime o valor em graus F e em graus C
print(f"{f}°F são {c}°C")