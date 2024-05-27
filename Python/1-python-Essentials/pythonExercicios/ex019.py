import random
al1 = input("Escreva o nome de um aluno ")
al2 = input("Escreva o nome de um aluno ")
al3 = input("Escreva o nome de um aluno ")
al4 = input("Escreva o nome de um aluno ")

listaDeAlunos = [al1, al2, al3, al4]
escolhido = random.choice(listaDeAlunos)

for aluno in listaDeAlunos:
    print(aluno)

print("O aluno escolhido foi o {}".format(escolhido))
