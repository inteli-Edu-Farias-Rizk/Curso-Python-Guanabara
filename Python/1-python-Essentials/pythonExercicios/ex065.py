media = 0
decisao = "S"
maior = 0
menor = 0
cont = 0

 
while decisao in "Ss":
    valor = int(input("Escreva o valor de algum número: "))
    cont += 1
    media += valor
    if cont == 1:
        menor = maior = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    decisao = input("Você deseja continuar [S/N] ").strip().upper()[0]
    
         
print("O maior valor digitado foi {} e o menor valor digitado foi {}, a média entre todos os valores é {}".format(maior,menor,media/cont))