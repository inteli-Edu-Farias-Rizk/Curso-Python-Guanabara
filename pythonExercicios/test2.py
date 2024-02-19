todos = []
while True:
    dic = {}
    lista = []
    dic["jogador"] = input("Qual o nome do jogador: ")
    partidas = int(input("Quantas partidas ele jogou: "))
    while partidas > len(lista):
        gols = int(input(f"Quantos gols na partida {len(lista) + 1}: "))
        lista.append(gols)
    dic['gols'] = lista
    dic['total'] = sum(lista)
    todos.append(dic.copy())

    resposta = input("Você gostaria de continuar (S/N): ")
    if resposta.upper() == "N":
        break
print('=-' * 40)
print(todos)
print('=-' * 40)

print('''
cod  nome          gols                    total
---------------------------------------------
''')
for indx, c in enumerate(todos):
    print(f"{indx:<5}", end="")
    for k, v in todos[indx].items():
        if k == 'jogador':
            print(f"{v:<15}", end="")
        if k == 'gols':
            print(f"{str(v):<25}", end="")
        elif k == 'total':
            print(v)
print("---------------------------------------------")

escolha = 80

while escolha != 999: 
    escolha = int(input("Mostrar dados de qual jogador [999 encerra]: "))
    for c in range(len(todos)):
        if escolha == c:
            for k,v in todos[c].items():
                if k == 'gols':
                    for x,y in enumerate(v):
                        print(f"No jogo {x} ele fez {y} gols")
            




