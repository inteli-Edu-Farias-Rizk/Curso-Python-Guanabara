soma = 0
count = 0
for num in range(1, 501):
    if num % 3 == 0 and num % 2 != 0:  # Verifica se é ímpar e múltiplo de 3
        soma += num #acumulador
        count += 1 #contador
print("A soma de todos  os números ímpares múltiplos de 3 de 1 até 500 é que são {} é {}".format(count, soma))




