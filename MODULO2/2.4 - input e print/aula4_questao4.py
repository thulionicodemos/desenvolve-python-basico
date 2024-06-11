#Entrada
x = int(input("Digite o valor em R$: "))

#Verifica a quantidade de notas de 100
notas100 = x//100
x = x-notas100*100

#Verifica a quantidade de notas de 50
notas50 = x//50
x = x-notas50*50

#Verifica a quantidade de notas de 20
notas20 = x//20
x = x-notas20*20

#Verifica a quantidade de notas de 10
notas10 = x//10
x = x-notas10*10

#Verifica a quantidade de notas de 5
notas5 = x//5
x = x-notas5*5

#Verifica a quantidade de notas de 2
notas2 = x//2
x = x-notas2*2

#Verifica a quantidade de notas de 1
notas1 = x//1
x = x-notas1

#Saída
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")