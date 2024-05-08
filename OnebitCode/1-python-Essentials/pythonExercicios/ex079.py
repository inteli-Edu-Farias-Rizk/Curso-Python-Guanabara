lista = []
while True:
    novoNum = int(input("Qual número você deseja add a sua lista: "))
    if novoNum not in lista:
        lista.append(novoNum)
    pergunta = " "
    while pergunta not in "SN":
        pergunta = input("Você quer continuar [S] ou [N]: ").upper().strip()[0]
    if pergunta == "N":
        break
lista.sort()    
print(lista)
    