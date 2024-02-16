import random
lista = []
cont = 0
pal = int(input("Quantos palpites voçê quer que sejam gerados: "))
for c in range (0,pal):
    temp = []
    cont = 0
    while cont < 6:
        num = random.randint(1,60)
        if num not in temp:
            temp.append(num)
            cont += 1
    lista.append(temp[:])
for i,jogos in enumerate(lista):
    print(f"O seu {i+1} jogo: {jogos}")
