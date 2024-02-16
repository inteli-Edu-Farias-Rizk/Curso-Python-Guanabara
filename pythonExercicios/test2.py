matriz = [[],[],[]]

pares = 0
terceira = 0
for l in range (0,3):
    for c in range(0,3):
        num = int(input(f"Qual a num voçê quer adicionar a {l} {c}: "))
        if c == 2:
            terceira += num
        if num % 2 == 0:
            pares += num
        matriz[l].append(num)
        
for l in range (0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]", end=" ")
    print()
    
maior = 0
    
for g in range (0,3):
    if maior < matriz[1][g]:
        maior = matriz[1][g] 
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma de todos os numeros da terceira coluna é {terceira}')
print(f"O maior valor da segunda linha é {maior}")       
