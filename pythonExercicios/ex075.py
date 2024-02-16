x = (int(input("Escreva um número: ", )), int(input("Escreva um número: ", )),int(input("Escreva um número: ", )),int(input("Escreva um número: ", )),int(input("Escreva um número: ", )))

print(f"Os valores digitados foram {x}")
par = 0
nove = 0 
tres  = 0
for c in range (0,5):
    if x[c] == 9:
        nove += 1
print(f"O numero 9 apreceu {nove} vez(es) e o 3 apareceu {tres} vez(es)") 
if 3 in x:
    print(f"O valor 3 apreceu na {x.index(3)+1} posição")
else:
    print("O numero 3 não se encontra na tupla")
print("Os numeros pares são: ")
for c in range (0,5):
    if x[c] % 2 == 0:
        print(f" {x[c]}", end = "")

        