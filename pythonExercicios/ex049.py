n1 = int(input("Qual número você deseja saber a tabuada: "))
print("A tabuada do {} é".format(n1))
for c in range(0,11):
    print("{} x {} = {}".format(n1,c,n1*c))