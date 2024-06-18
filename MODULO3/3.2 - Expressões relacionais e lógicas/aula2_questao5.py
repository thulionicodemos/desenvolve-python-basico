gen = str(input("Qual seu gênero (M ou F): "))
idade = int(input("Digite sua idade: "))
tServico = int(input("Qual seu tempo de serviço (em anos): "))

if gen == 'F':
    if (idade > 60) or (tServico >= 30) or (idade >= 60 and tServico >= 25):
        print("Já pode aposentar? ", True)
    else:
        print("Já pode aposentar? ", False)
elif gen == 'M':
    if (idade > 65) or (tServico >= 30) or (idade >= 60 and tServico >= 25):
        print("Já pode aposentar? ", True)
    else:
        print("Já pode aposentar? ", False)
else:
    print("Entrada inválida!")