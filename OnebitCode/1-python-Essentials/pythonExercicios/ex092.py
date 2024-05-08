import datetime

dic = {}
dic["ctps"] = 1
while True:
    dic["nome"] = input("Qual é o nome: ").capitalize() #garante que a primeira letra seja em maiuscula
    ano_nascimento = int(input("Qual o seu ano de nascimento: "))
    dic["idade"] = datetime.datetime.now().year - ano_nascimento

    dic["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))
    if dic["ctps"] == 0:
        break

    dic["contratação"] = input("Ano de contratação: ")
    dic["salário"] = round(float(input("Salário: ")), 2)  # Convertido para float para representar valores monetários em duas casas decimais

    break

print("=+" * 30)
print("Informações:")
for chave, valor in dic.items():
    print(f"{chave}: {valor}")
