classe = str(input("Escolha sua classe! (mago, guerreiro ou arqueiro): "))
forca = int(input("Atribua os pontos de força (de 1 a 20): "))
magia = int(input("Agora atribua os pontos de magia(de 1 a 20): "))

if classe == 'mago':
    if forca <= 10 and magia >= 15:
        print("Pontos de atributo consistentes com a classe escolhida: ", True)
    else:
        print("Pontos de atributo consistentes com a classe escolhida: ", False)
        
elif classe == 'guerreiro':
    if forca >= 15 and magia <=10:
        print("Pontos de atributo consistentes com a classe escolhida: ", True)
    else:
        print("Pontos de atributo consistentes com a classe escolhida: ", False)
    
elif classe == 'arqueiro':
    if (forca > 5 and forca < 15) and (magia > 5 and magia < 15):
        print("Pontos de atributo consistentes com a classe escolhida: ", True)
    else:
        print("Pontos de atributo consistentes com a classe escolhida: ", False)

else:
    print("Classe inválida!")