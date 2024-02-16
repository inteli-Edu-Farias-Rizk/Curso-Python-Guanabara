n1 = int(input("Escreva o valor de um número: "))
n2 = int(input("Escreva o valor de outro número: "))
print("-="*15)
rodar = False
while not rodar:
    print(''' 
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        ''')
    print("-="*15)
    menu = int(input("Escreva qual das funcionalidades você gostaria de adotar: "))
    if menu == 1:
        print("A soma de {} com {} é {}".format(n1, n2, n2 + n1))
        rodar = True
    elif menu == 2:
        print("A multiplicação de {} e {} é {}".format(n1, n2 , n1 * n2))
        rodar = True
    elif menu == 3:
        if n1 > n2:
            print("O maior numero entre {} e {} é {}".format(n1,n2,n1))
            rodar = True
        else:
            print("O maior numero entre {} e {} é {}".format(n1,n2,n2))
            rodar = True    
    elif menu == 4:
            n1 = int(input("Escreva o valor do seu novo número: "))
            n2 = int(input("Escreva o valor do seu outro novo número: "))
    else:
        rodar = True
            
            
if rodar == True:
    print("Encerrou o programa")