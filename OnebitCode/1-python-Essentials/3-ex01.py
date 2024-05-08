def verifica(palavra):
    Maisc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Minusc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Pmin = []
    Pmai = []
    contMai = 0
    contMin = 0
    for i in palavra:
        if i in Maisc:
            contMai += 1
            Pmai.append(i)
        if i in Minusc:
            contMin += 1
            Pmin.append(i)
    return Pmin, contMin, Pmai, contMai

palavra_usuario = input("Digite uma palavra: ")
Pmin, contMin, Pmai, contMai = verifica(palavra_usuario)
print(f"As letras minúsculas que tinha na palavra eram: {Pmin}, totalizando {contMin}, e as maiúsculas eram {Pmai}, totalizando {contMai}")

