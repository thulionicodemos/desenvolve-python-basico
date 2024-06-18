idade = int(input("Digite sua idade: "))
jogos = str(input("Já jogou pelo menos 3 jogos de tabuleiro? (True ou False): "))
vitorias = int(input("Quantos jogos já venceu? "))

if (idade >= 16 and idade <=18) and (jogos == "True") and (vitorias >= 1):
    print("Apto para ingressar no clube de jogos de tabuleiro: ", True)
else:
    print("Apto para ingressar no clube de jogos de tabuleiro: ", False)