c = 0 
n1 = 0
cont = 0
while n1 != 999:
    n1 = int(input("Escreva o valor de um número: "))
    if n1 == 999:
        print("Acabou")
    else:
        c += n1
        cont += 1
print("A soma de {} números digitados é {}".format(cont, c))