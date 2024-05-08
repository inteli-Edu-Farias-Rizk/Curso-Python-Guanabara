n1 = int(input("Qual número você quer que o fatorial seja mostrado: "))
c = n1
multiplicador = 1
while c > 0:
    
    multiplicador = c * multiplicador
    c = c - 1
print(multiplicador)