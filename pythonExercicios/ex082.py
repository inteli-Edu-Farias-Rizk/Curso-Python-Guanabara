lista = []
pares = []
impar = []
while True:
    num = int(input("Qual número você quer adiconar a lista: "))
    lista.append(num)
    dec= " "
    while dec not in "NnSs":
        dec = input("Voçê deseja continuar? [S] [N]: ").upper().strip()[0]
    if dec == "N":
        break
cont = 0
while cont < len(lista):
    if lista[cont] % 2 == 0:
        pares.append(lista[cont])
    else:
        impar.append(lista[cont])
    cont += 1
print(f"Essa é a lista do pares {pares}, e essa é a lista do impares {impar}")
print("="*30)
lista.sort()
print(lista)