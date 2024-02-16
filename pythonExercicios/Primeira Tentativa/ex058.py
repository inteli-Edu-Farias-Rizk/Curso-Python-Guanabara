import random
tentativas = 0
CompNum = random.randint(0,10)
while True:
    guess = int(input("Qual numero de 0 a 10 o computador estava pensando? "))
    tentativas += 1
    if guess == CompNum:
        if tentativas == 1:
            print(f"Foi nescessário {tentativas} tenativa")
        else:
            print(f"Foram nescessárias {tentativas} tenativa(s)")
        break
    elif guess < CompNum:
        print("O numero pensado é maior tente novamente:")
    else:
        print("O numero pensado é menor tente novamente")