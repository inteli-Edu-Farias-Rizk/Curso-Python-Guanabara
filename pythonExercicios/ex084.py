list = []
total = []
pesoMenor = pesoMaior = 0
nomeMenor = [] #Nome das pessoas que pesam meno kilos
nomeMaior = []

num = 0
while True:
    num += 1
    Nome = input("Qual o nome da pessoa que quer ser cadastrada: ")
    peso = int(input("Quanto ela pesa: "))
    
    list.append(Nome)
    list.append(peso)
    total.append(list[:])
    list.clear()
    dec= " "
    while dec not in "NnSs":
        dec = input("Voçê deseja continuar? [S] [N]: ").upper().strip()[0]
    if dec == "N":
        break
count = 0
for c in total:
    if count == 0 or pesoMenor > c[1] :
        pesoMenor = c[1]
        nomeMenor = [c[0]] 
    elif pesoMenor == c[1]:
        nomeMenor.append(c[0])
    if count == 0 or pesoMaior < c[1]:
        pesoMaior = c[1]
        nomeMaior = [c[0]]
    elif pesoMaior == c[1]:
        nomeMaior.append(c[0])
    count+=1
print("="*30)
print(f"A é composta pelos nomes de {total} ")
print(f"Você cadastrou um total de {num} pessoas")
print(f"O maior peso foi de {pesoMaior}kg que foi/foram de {nomeMaior}")
print(f"O menor peso foi de {pesoMenor}kg que foi/foram de {nomeMenor}")    