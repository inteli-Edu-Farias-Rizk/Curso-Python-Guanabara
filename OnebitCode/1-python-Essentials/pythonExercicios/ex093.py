dic = {}
dic["gols"] = []
dic["nome"] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {dic['nome']} jogou: "))
for c in range(partidas):
    num = int(input((f"Quantos gols na partida {c+1}? ")))
    dic["gols"].append(num)
dic['total'] = sum(dic['gols'])
print("=+" *30)
for ind, valor in dic.items():
     print(f"O campo {ind} tem o valor {valor} ")
print("=+" *30)
for c,v in enumerate(dic["gols"]):
    print(f"Na partida {c+1} ele fez {v} gols ")
    
print(f"No total foi feito {dic['total']} gols")
