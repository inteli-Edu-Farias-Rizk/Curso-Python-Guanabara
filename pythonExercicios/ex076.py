listagem = ("Pao", 1.00 , "Peito de Peru",10.9, "Queijo", 3.75,"Farinha",4.25, "Açúcar", 5.00, "Massa", 6.75 )
cont = 0
print("--"*40)
print("                             TABELA DE PREÇOS")
print("--"*40)
while True:
    print(listagem[cont],"..." * 20,end="")
    cont += 1
    print("$",listagem[cont])
    cont += 1
    if cont == 12:
        break
print("--"*40)
print("O que você vai querer?")