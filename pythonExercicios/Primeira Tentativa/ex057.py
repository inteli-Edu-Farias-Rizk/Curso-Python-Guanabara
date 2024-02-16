while True:
    sexo = input("Qual o seu sexo? masculino [M] feminino [F]: ").upper().strip()[0]
    if sexo in "MF":
        break
if sexo == "M":
    print("O seu sexo é masculino")
if sexo == "F":
    print("O seu sexo é feminino")