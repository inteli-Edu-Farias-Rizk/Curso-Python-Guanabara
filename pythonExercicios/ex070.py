total = 0
mil = 0
barato = ""
contador  = 0
menor = 0
while True:
    nome = input("Nome do produto: ")
    preco = int(input("Qual é o preço desse produto: "))
    total += preco
    contador += 1
    if preco > 1000:
        mil += 1
    if contador == 1 or preco < menor:
        barato = nome
        menor = preco
    cont = " "
    while cont not in "NS":
        cont = input("Quer continuar?  [S/N] ").strip().upper()[0]
    if cont == "N":
        break
print(f" O total da compra foi {total} tem {mil} produto(s) acima de mil reais e o produto mais barato foi {barato} custando {menor} reais")

    