dic = {}
lista = []
dic["jogador"] = input("Qual o nome do jogador: ")
partidas = int(input("Quantas partidas ele jogou: "))
while partidas > len(lista):
    gols = int(input(f"Quantos gols na partida {len(lista) + 1}: "))
    lista.append(gols)
dic['gols'] = lista
dic['total'] = sum(lista)
print('=-' * 40)
print(dic)
print('=-' * 40)
print(f"O jogador {dic['jogador']} jogou {partidas} partidas ")
cont = 0
for c in lista:
    print(f"Na partida {cont +1}, fez {c} gols")
    cont += 1
print(f"Foi um total de {dic['total']}")