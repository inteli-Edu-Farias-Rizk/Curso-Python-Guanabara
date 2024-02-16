masc = 0
fem = 0
cont = 0
while True:
    print("=" * 30)
    print("     CADASTRE UMA PESSOA")
    print("=" * 30)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo [M/F]: ").strip().upper()[0]
    if idade > 18:
        cont += 1
    if sexo in "Mm":
        masc += 1
    if sexo in "F" and idade < 20:
        fem += 1
    print("=" * 30)
    abd =" "
    while abd not in "SN":
        abd = input("Quer continuar? [S/N]: ").strip().upper()[0]
    if abd in "Nn":
        break
    print("=" * 30)
print(f"Tem {cont} cadastradas maiores de 18 anos,  sendo {fem} mulheres abaixo de 20 anos e {masc} homens ")