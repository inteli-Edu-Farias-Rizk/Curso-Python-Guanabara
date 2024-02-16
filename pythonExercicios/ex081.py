lista = []
count = 0

while True:
    num = int(input("Qual número você gostaria de adicionar: "))
    lista.append(num)
    count += 1
    dec = " "
    while dec not in "NSsn":
        dec = input("Voce gostaria de continuar? ").strip().upper()[0]
    if dec == "N":
        break
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O 5 não está na lista")
lista.sort(reverse=True)
print(lista)