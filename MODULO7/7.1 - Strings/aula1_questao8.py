def validador_cpf(cpf):
    # Remove os caracteres não numéricos do CPF
    cpf = cpf.replace('.', '').replace('-', '')
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    if soma % 11 < 2:
        digito1 = 0
    elif soma % 11 >= 2:
        digito1 = 11 - (soma % 11)

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    if soma % 11 < 2:
        digito2 = 0
    elif soma % 11 >= 2:
        digito2 = 11 - (soma % 11)
    
    # Verifica se os dígitos verificadores estão corretos
    if cpf[-2:] == f"{digito1}{digito2}":
        return True
    else:
        return False

cpf_usuario = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")

if validador_cpf(cpf_usuario):
    print("CPF Válido")
else:
    print("CPF Inválido")