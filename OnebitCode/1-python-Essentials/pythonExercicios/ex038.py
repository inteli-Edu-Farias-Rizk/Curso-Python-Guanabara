n1 = int(input("Escreva o valor de um número: "))
n2 = int(input("Escreva o valor de outro número: "))

if n1 > n2:
    print(" o valor {} é maior que o valor {}".format(n1, n2))
elif n1 < n2:
    print(" o valor {} é maior que o valor {}".format(n2, n1))
else: 
    print(" O valor dos números são iguais")