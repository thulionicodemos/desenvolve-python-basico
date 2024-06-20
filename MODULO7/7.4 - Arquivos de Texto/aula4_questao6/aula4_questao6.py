import csv

# Processamento do arquivo para extrair informações
top_songs = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as file:
    csv_reader = csv.reader(file)
    # Pular cabeçalho
    next(csv_reader)  
    for line in csv_reader:
        # Verificar se a linha possui o número correto de elementos
        if len(line) < 9:  # Verificar se há pelo menos 9 elementos na linha
            continue  # Ignorar linhas com formatação inválida

        # Extrair informações relevantes
        track_name = line[0]
        artist_name = line[1]
        released_year = int(line[3])
        
        # Converte o número de streams para inteiro
        try:
            streams = int(line[8])
        except ValueError:
            continue  # Ignorar linhas com formatação inválida

        # Verificar se a música está dentro do intervalo de 2012 a 2022
        if 2012 <= released_year <= 2022:
            # Verificar se é a música mais tocada do ano
            if released_year not in top_songs or streams > top_songs[released_year][3]:
                top_songs[released_year] = [track_name, artist_name, released_year, streams]

for song in sorted(top_songs.values(), key=lambda x: x[2]):
    print(song)