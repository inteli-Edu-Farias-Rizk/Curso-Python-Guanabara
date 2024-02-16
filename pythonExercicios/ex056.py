total = 0
hmv = 0 #A idade do homem mais velho 
mm20 = 0 #Para ver quantas mulheres sãomenores que 20 anos
for c in range (1,5):
    idade = int(input("Qual é a sua idade: "))
    nome = input("Qual é o seu nome: ")
    sexo = int(input("O seu sexo é [1] Masculino [2] Feminino: "))
    total += idade
    if sexo == 1 and hmv < idade:
        hmv = idade
    if sexo == 2 and idade < 20:
        mm20 += 1
        
media = total / 4
print("A média de idade do grupo é {}") .format(media)
print ("A idade do homem mais velho é {}".format(hmv))
print("O números de mulheres abaixo de 20 anos é {}".format(mm20))