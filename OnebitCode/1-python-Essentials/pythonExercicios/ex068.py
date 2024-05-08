
import random
cont = 1
while True:
    n1 = int(input("Digite um valor: "))
    jog = input("Par ou Ímpar?  [P/I]: ").strip().upper()[0] 
    comp = random.randint(1,10)
    soma = n1 + comp
    print(f"Você jogou {n1} e o computador jogou {comp} total deu {soma}")
    if soma % 2 == 0:
        if jog in "Pp":
            print("Você venceu!!")
            print("Vamos jogar novamente....")
            cont += 1
        else:
            print(f"Você perdeu em {cont} jogadas")
            break
    else:
        if jog in "Ii":
            print("Você venceu!!")
            print("Vamos jogar novamente.....")
            cont += 1
        else:
            print(f"Você perdeu em {cont} jogada(s)")
            break
        