i = n = int(input("Digite o número de experimentos realizados: "))

totalCobaia, sapos, ratos, coelhos = (0, 0, 0, 0)

while i > 0:
    quantCobaia = int(input("Digite quantidade de cobaias utilizadas: "))
    tipoCobaia = str(input("Digite o tipo de cobaia (S: Sapo, R: Rato ou C: Coelho): "))

    totalCobaia += quantCobaia

    if tipoCobaia == 'S':
        sapos += quantCobaia
    elif tipoCobaia == 'R':
        ratos += quantCobaia
    elif tipoCobaia == 'C':
        coelhos += quantCobaia
    else: 
        print("Tipo inválido!")

    i -= 1

percS = sapos/totalCobaia*100
percR = ratos/totalCobaia*100
percC = coelhos/totalCobaia*100

print(f"Total: {totalCobaia} cobaias")
print(f"Total de sapos: {sapos}")
print(f"Total de ratos: {ratos}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de sapos: {percS:.2f}%")
print(f"Total de ratos: {percR:.2f}%")
print(f"Total de coelhos: {percC:.2f}%")