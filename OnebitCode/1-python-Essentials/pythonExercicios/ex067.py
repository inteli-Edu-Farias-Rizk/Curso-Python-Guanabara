while True:
    n1 = int(input("Você quer saber a tabuada de qual valor: "))
    if n1 < 0:
        break
    print("=-" * 30)
    for c in range (1,11):
        print(f"{n1} x {c} = {n1*c}")
    print("=-" * 30)

print("ERROR")