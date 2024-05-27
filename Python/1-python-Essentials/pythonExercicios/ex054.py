from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nascimento = int(input("Escreva a sua data de nascimento: "))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("Tem {} maiores de idade e {} menores de idade".format(maior, menor))