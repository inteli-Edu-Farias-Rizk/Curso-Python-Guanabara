import random

acertou = False
palpite = 0
computador = random.randint(0, 10)
print("O computador acabou de pensar em um número de 0 a 10.")

while acertou == False:
    chute = int(input("Qual valor de 0 a 10 você acha que foi pensado pelo computador: "))
    palpite += 1

    if chute == computador:
        acertou = True
        print("Parabéns! Você acertou o número pensado em {} tentativa(s) e o número pensado foi {}.".format(palpite, computador))
    elif chute < computador:
        print("O número pensado é maior. Tente novamente.")
    else:
        print("O número pensado é menor. Tente novamente.")


        
            

    


