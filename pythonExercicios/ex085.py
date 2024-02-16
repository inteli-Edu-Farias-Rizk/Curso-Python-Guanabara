lista = [[],[]]
for c in range(0,7):
    num = int(input("Qual o prox valor que voçê gostaria de adicionar: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(lista)
lista[0].sort()
lista[1].sort()
print(lista) 