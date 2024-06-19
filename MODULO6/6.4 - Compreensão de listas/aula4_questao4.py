alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Lista de aprovados utilizando compreensão de listas
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

print(aprovados)