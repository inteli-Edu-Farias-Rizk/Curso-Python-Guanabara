from random import randint

num = randint(0,10)
qnt = 0
while True:
    tent = int(input("Qual número você chutaria: "))
    qnt += 1
    if tent == num:
        print('Voçê acertou sua tentativa.')
        break
