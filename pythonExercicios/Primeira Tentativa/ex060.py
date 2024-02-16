num = int(input("Qual número você quer fazer o seu fatorial: "))

fatorial = 1
while True: 
    fatorial = num * fatorial
    num -= 1
    if num == 0:
        break
print (fatorial)
    
    