cont = 0
soma = 0
while True:
    n1 = int(input("Escreva o valor de um número: "))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f"Foram digitados  {cont} e a soma entre eles é {soma}")
    