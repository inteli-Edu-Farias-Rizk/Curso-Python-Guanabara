total = []
temp = [] #vai guardar o nome, a lista com as duas notas, além da média
notas = []

while True:
    temp = [] #vai guardar o nome, a lista com as duas notas, além da média
    notas = []
    nome = input("Qual o nome do aluno: ")
    temp.append(nome)
    #pegando as notas e guardando em uma lista
    nota1 = int(input("Qual a primeira nota: "))
    notas.append(nota1)
    nota2 = int(input("Qual a sua segunda nota: "))
    notas.append(nota2)
    
    temp.append(notas[:])
    
    media = (nota1 + nota2)/2
    temp.append(media)
    total.append(temp[:])
    temp.clear() 
    resp = " "
    while resp not in "NnSs":
        resp = input("Voçê deseja continuar? [S] [N]: ").upper().strip()[0]
    if resp == "N":
        # Break out of the loop if the user chooses not to continue
        break
print(total)

print("Boletim:")
for idx, aluno in enumerate(total):
    print(f"Aluno {idx}: {aluno[0]}, Média: {aluno[2]}")
escolha = int(input("Qual aluno voçê gostaria que fosse mostrado: "))
for idx, aluno in enumerate(total):
    if idx == escolha:
        print("As notas foram: ")
        for c in total[idx][1]:
            print(f"A nota é: {c}")

    
    
    




    