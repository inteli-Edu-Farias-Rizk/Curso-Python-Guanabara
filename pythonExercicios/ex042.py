r1 = float(input("Primeiro segmento de reta: "))
r2 = float(input("Segundo segmento de reta: "))
r3 = float(input("Terceiro segmento de reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Pode ser formado um triangulo! ")
    if r1 == r2 == r3:
        print("Escaleno")
    elif r1 != r2 != r3 != r1: 
        print("Escaleno")
    else:
        print("isóceles")
else:
    print("Não pode ser formado um triangulo ")
