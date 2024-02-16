import math
cat1 = float(input("Escreva o valor do primeiro cateto: "))
cat2 = float(input("Escreva o valor do segundo cateto:"))
resultado = cat1 ** 2 + cat2 ** 2

print("A hipotenusa é {:.0f}".format(math.sqrt(resultado)))

