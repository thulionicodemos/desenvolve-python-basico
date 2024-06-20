def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        return False
    
    # Verifica se a senha contém pelo menos uma letra minúscula
    if not any(char.islower() for char in senha):
        return False
    
    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    
    # Verifica se a senha contém pelo menos um caractere especial
    caracteres_especiais = "@#$%^&*()_+[]{}|;:,.<>?/`~!\"\\"
    if not any(char in caracteres_especiais for char in senha):
        return False
    
    return True

# Exemplo de uso:
senha = input("Digite sua senha: ")

print(validador_senha(senha))