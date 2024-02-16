matriz = [[],
          [],
          []
          ]
count = 0
pares = 0
somaTerceira = 0
while count < 3:
    for c in range(0,3):
        num = int(input(f"DIgite um valor para [{count},{c}]: "))
        if c == 2:
            somaTerceira += num
        if num % 2 == 0:
            pares += num    
        matriz[count].append(num)
    count += 1
print(matriz)
print("++"*30)

for p in matriz[0]:
    print(f"[{p:^5}]" ,end="")

print()

maiorValor = 0
for x in matriz[1]:
    print(f"[{x:^5}]", end="")
    if maiorValor < x:
        maiorValor = x
        
print()


for t in matriz[2]:
    print(f"[{t:^5}]", end ="")
print()
print(f"A soma de todos os valores pares é {pares} a soma dos valores da terceira coluna é {somaTerceira}")
print(f"O maior valor da segunda linha é {maiorValor}")    