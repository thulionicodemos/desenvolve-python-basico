# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista de domínios extraídos
dominios = []
for url in urls:
    dominio = url[4:-4]
    dominios.append(dominio)

print(f"URLs: {urls}")
print(f"Domínios: {dominios}")