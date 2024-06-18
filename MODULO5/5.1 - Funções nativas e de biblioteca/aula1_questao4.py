from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

# Exibe a data e hora formatadas
print(f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}")
print(f"Hora: {agora.hour:02d}:{agora.minute:02d}")
