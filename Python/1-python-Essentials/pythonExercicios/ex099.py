def maior(*d):
    maior = 0
    cont = 0 
    print("Analisando os valores : ")
    for valor in d:
        print(f"{valor}", end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores")
    print(f"Sendo o maior deles esse {maior}")
           
    
    
    
    
    # if cont == 0:
    #     print("Foram informado 0 valores ao todo ")
    #     print("O maior valor informado foi 0")
    # print(f"O maior valor é {maior}")
maior()