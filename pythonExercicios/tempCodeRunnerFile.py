lista  = []
while True:
    dic = {}
    dic["nome"] = input("Qual seu nome: ").capitalize()
    dic["sexo"] = input("Qual seu sexo [M/F]: ").upper().strip()[0]
    dic["idade"] = int(input("Qual a sua idade: "))
    lista.append(dic)
    resposta = input("Você gostaria de continuar (S/N): ")
    if resposta.upper() == "N":
        break

somaIdade = 0
mulheres = []
cadastrados = len(lista)

for c in lista:
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
    somaIdade += c['idade']

media = somaIdade / cadastrados

acimaMedia = []
for x in lista:
    if x['idade'] > media:
        acimaMedia.append(x['nome'])

print(f"Foram cadastradas {cadastrados} pessoas")
print(f"As mulheres são essas: {mulheres}")
print(f"As pessoas com idade acima da média são essas: {acimaMedia}")



print(f"Foram cadastradas {cadastrados} pessoas")
print(f"As mulheres são essas {mulheres}")
print(f"As pessoas com idade acima da media são essas {acimaMedia}")


        
