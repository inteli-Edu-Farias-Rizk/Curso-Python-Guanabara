from time import sleep
t1 = int(input("Qual o primeiro termo da sua PA: "))
r = int(input("Qual a razão da PA: "))

cont = 1
while cont <= 10:
    an = t1 + (cont - 1) * r
    sleep(0.5)
    print(an) 
    cont += 1
    