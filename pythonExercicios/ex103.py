def ficha(nome='desconhecido', gols=0):
    return f'O jogador {nome}, fez {gols} gols'

# Solicitando ao usuário o nome do jogador e a quantidade de gols
nome_jogador = input("Qual o nome do jogador: ")
gols_jogador = input("Quantos gols ele fez: ")

# Verificando se o usuário deixou o campo de gols em branco e atribuindo 0 nesse caso a função gisnumeric() verifica se foi digitado uma string
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

# Chamando a função ficha com os valores fornecidos pelo usuário
resultado = ficha(nome_jogador, gols_jogador)

# Imprimindo o resultado
print(resultado)
