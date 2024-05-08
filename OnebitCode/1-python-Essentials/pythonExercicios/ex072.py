tupla = ("zero","um","dois","tres","quatro","cinco")
while True:
    numero = int(input("Escreva um número de 0 a 5: "))
    if  0 <= numero <=5:
        print(f"O numero escrito por extenso é {tupla[numero]}")
        break
    