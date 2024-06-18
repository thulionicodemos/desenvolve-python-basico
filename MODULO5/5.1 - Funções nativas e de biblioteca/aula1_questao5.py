import emoji

# Lista de emojis disponíveis
emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

# Exibe lista de emojis disponíveis
print("Emojis disponíveis:")
for codigo, icone in emojis_disponiveis.items():
    print(f"{icone} - {codigo}")

frase = input("\nDigite uma frase e ela será emojizada: ")

# 'Emojizar' a frase
frase_emojizada = emoji.emojize(frase, language='alias')

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)
