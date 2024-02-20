numeros = []
def sorteia():
    import random
    for c in range(0,5):
        num = random.randint(1,100)
        numeros.append(num)
        
def somaPar():
    soma = 0
    for c in numeros:
        print(c, end =" ")
        if c % 2 == 0:
            soma += c
    print()
    print(soma)
sorteia()
somaPar()
