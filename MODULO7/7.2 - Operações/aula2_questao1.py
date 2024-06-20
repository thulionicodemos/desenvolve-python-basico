data = str(input("Digite uma data de nascimento: "))

# Lista com meses do ano
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Divide a data em dia, mês e ano
dia, mes, ano = data.split('/')

print(f"Você nasceu em {dia} de {(meses[int(mes) - 1])} de {ano}.")