import random
j1 = int(input("(1)Tesoura (2) Pedra (3) Papel"))
j2 = int(input(random.randint(1,3)))
if j1 == j2:
    print("Empate")
elif j1 == 1 and j2 == 2:
    print("O jogador 2 ganhou porque pedra ganha de papel")
elif j1 == 2 and j2 == 1:
    print("O jogador 1 ganhou porque pedra ganha de papel")
elif j1 == 2 and j2 == 3:
    print("O jogador 1 ganhou pois papel ganha de pedra")
elif j1 == 3 and j2 == 2:
    print("O jogador 1 ganhou pois papel ganha de pedra")
 


