sexo = input("Escreva qual o seu sexo (M) ou (F) : ").strip().upper()[0]
while sexo != "M" and sexo != "F":
    sexo = input("Dados inválidos por favor nos dê seu sexo: ").upper().strip()[0] #0 = só pega a primeira letra
print("Sexo {} registrado com sucesso".format(sexo))