todos = []

while True:
    dic = {}
    dic["gols"] = []
    dic["nome"] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {dic['nome']} jogou: "))

    for c in range(partidas):
        num = int(input((f"Quantos gols na partida {c+1}? ")))
        dic["gols"].append(num)
    dic['total'] = sum(dic['gols'])
    todos.append(dic)
    resposta = input("Voçê gostaria de continuar: ")
    if resposta in "Nn":
        break
    
    
jogador  = input("Mostrar os dados de qual jogador: ")
for c in todos[jogador]:
    print(c)



