import random
jogos = []
temp = []
tentativas  = int(input("Quantos jogos você gostaria de fazer: "))
for c in range (tentativas):
    while len(temp) < 6:
        num = random.randint(1,60)
        if num not in temp:
            temp.append(num)
    temp.sort()
    jogos.append(temp[:])
    temp.clear()   
cont = 0 
for i,jogadas in enumerate(jogos):
    print(f"Essa é a jogada {i+1}: {jogadas}")