import random

# Pega uma palavra aleatória do arquivo em questão
def carregar_palavra():
    with open('gabarito_forca.txt', 'r') as f:
        palavras = f.readlines()
    return random.choice(palavras).strip()

def carregar_estagios():
    with open('gabarito_enforcado.txt', 'r') as f:
        estagios = f.read().split('\n\n')
    return estagios

def imprime_enforcado(estagios, erros):
    print(estagios[erros])
    
def jogo_da_forca():
    palavra = carregar_palavra()
    estagios = carregar_estagios()
    palavra_oculta = ['_' for _ in palavra]
    tentativas = set() # Armazena a letra que já foi inserida
    erros = 0

    print("Bem-vindo ao jogo da forca!\n")
    print(' '.join(palavra_oculta))

    # Loop que continua até o jogador adivinhar a palavra ou perder todas as tentativas
    while erros < 6 and ''.join(palavra_oculta) != palavra:
        tentativa = input("\nDigite uma letra: ").lower()
        
        if tentativa in tentativas:
            print("\nVocê já tentou essa letra. Tente outra.")
            continue
        
        tentativas.add(tentativa)
        
        # Verificaa se a letra está na palavra
        if tentativa in palavra:
            for idx, letra in enumerate(palavra):
                if letra == tentativa:
                    palavra_oculta[idx] = tentativa # Substitui o " _ " pela letra correta
        else:
            erros += 1

        print(' '.join(palavra_oculta))
        imprime_enforcado(estagios, erros)
        print(f"\nTentativas erradas: {erros}/6")

    if ''.join(palavra_oculta) == palavra:
        print("\nParabéns! Você adivinhou a palavra.")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()