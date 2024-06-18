n = int(input("Digite a quantidade de respondentes: "))
if n <= 0:
    print("O número de respondentes deve ser positivo.")

else:

    i = 1
    idade = 0
    m = 0

    while i <= n:
        idade = int(input(f"Digite {i}ª idade: "))
        if idade < 0:
            print("Erro: Idade não pode ser negativa. Tente novamente.")
            continue

        m += idade
        i += 1

    print("A média das idades é: ", m/n, "anos")