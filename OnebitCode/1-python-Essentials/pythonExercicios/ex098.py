def contador(inicio, fim, passo):
    if passo < 0: #se o usuário me dar um valor negativo de passo eu vou transformar em positivo, ajustando o programa.
        passo *= -1
    if passo == 0:
        passo = 1

    print("~~" *20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(cont, end = " ")
            cont -= passo
        print("FIM")
        print()
    else:
        cont = inicio
        while cont <= fim:
            print(cont, end = " ")
            cont += passo
        print("FIM")
        print()
    
    
contador(1,10,1)
contador(10,0,2)
contador(int(input("Incio: ")),int(input("Fim: ")),int(input("Passo: ")))

