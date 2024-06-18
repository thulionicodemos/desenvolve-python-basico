import random

#gerar um número aleatório entre 1 e 10
n = random.randint(1, 10)
    
while True:
    #pede ao usuário para adivinhar o número
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
        
    #fornecer feedback ao usuário
    if palpite < n:
        print("Muito baixo!")
    elif palpite > n:
        print("Muito alto!")
    else:
        print(f"Correto! O número é {n}.")
        break