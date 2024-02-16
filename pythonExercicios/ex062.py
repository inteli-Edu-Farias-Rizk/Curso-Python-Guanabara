p1 = int(input("Qual o primeiro termo da PA: "))
razao = int(input("Qual a razão: "))
c = 1
mais = 1
while mais != 0: 
    while c <= 10:
        an = p1 + (c - 1) * razao 
        print(an, end = "-> ")
        c += 1
    mais = int(input("Quantos termos a mais você quer que seja mostrado? "))
    for i in range (0, mais):
        an = p1 + (c - 1) * razao 
        print(an, end = "-> ")
        c += 1
    print("Pausa")