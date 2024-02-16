from time import sleep
t1 = int(input("Qual o primeiro termo da sua PA: "))
r = int(input("Qual a razão da PA: "))
cont = 1
mais = 1
while mais != 0:
    while cont <= 10:
        an = t1 + (cont - 1) * r
        print(an) 
        cont += 1
    mais = int(input("Quantos termos a mais você quer que mostre: "))
    for c in range (0,mais):
        an = t1 + (cont - 1) * r
        print(an) 
        cont +=1
         
