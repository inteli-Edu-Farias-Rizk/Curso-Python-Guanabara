import random

al1 = input("Escreva o nome de um aluno: ")
al2 = input("Escreva o nome de um aluno: ")
al3 = input("Escreva o nome de um aluno: ")
al4 = input("Escreva o nome de um aluno: ")

listaDeAlunos = [al1, al2, al3, al4]

# Embaralhar a lista
random.shuffle(listaDeAlunos)

print("A lista de alunos reorganizada é:")
for x in listaDeAlunos:
    print(x)
