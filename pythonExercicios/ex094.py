lista  = []
while True:
    dic = {}
    dic["nome"] = input("Qual seu nome: ").capitalize()
    dic["sexo"] = input("Qual seu sexo [M/F]: ").upper().strip()[0]
    dic["idade"] = int(input("Qual a sua idade: "))
    lista.append(dic)
    resposta = input("Voçê gostaria de continuar: ")
    if resposta in "Nn":
        break
print(lista)
print(f"O total de pessoas cadastradas foi {len(lista)}")
mulheres = []
cont = 0
for c in range(len(lista)):
    for ind,valor in lista[c].items():
        if ind == "idade":
            cont += valor
        if ind == "sexo":
            if valor == "F":
                mulheres.append(lista[c]["nome"])
                
media = cont/len(lista)
print(f"A media de idade é {media:.2f}")

print("Mulheres:")
print(mulheres)

acimaMedia = []
for c in range(len(lista)):
    for ind,valor in lista[c].items():
        if ind == "idade":
            if valor > media:
                acimaMedia.append(lista[c])
print("Pessoas acima da media: ")
print(acimaMedia)
                            