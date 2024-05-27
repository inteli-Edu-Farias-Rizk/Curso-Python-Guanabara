from random import randint
from time import sleep
from operator import itemgetter

# Inicializa um dicionário 'jogo' com 4 jogadores e atribui valores aleatórios de 1 a 6 a cada jogador
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

# Inicializa uma lista vazia 'ranking' que será usada para armazenar a classificação dos jogadores
ranking = []

# Imprime os valores sorteados para cada jogador
print("Valores sorteados:")
for i, v in jogo.items():
    print(f"{i} tirou {v} no dado.")
    sleep(0.5)  # Aguarda 0.5 segundos antes de imprimir o próximo jogador

# Classifica o dicionário 'jogo' com base nos valores (números aleatórios) em ordem decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Imprime o ranking com a posição de cada jogador e seu respectivo valor
print("Ranking:")
for i, v in enumerate(ranking, start=1):
    print(f"{i} lugar {v[0]} com {v[1]}")
