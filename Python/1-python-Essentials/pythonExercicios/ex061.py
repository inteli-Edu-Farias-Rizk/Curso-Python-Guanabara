p1 = int(input("Qual o primeiro termo da PA: "))
razao = int(input("Qual a razão: "))
c = 1
an = p1 + (c - 1) * razao
while c <= 10:
    an = p1 + (c - 1) * razao 
    print(an, end = "-> ")
    c += 1
print("Acabou")