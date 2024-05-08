# Inicialização de uma matriz vazia com três listas vazias
matriz = [[], [], []]

# Loop aninhado para percorrer as linhas e colunas da matriz
for l in range(0, 3):  # Itera sobre as linhas (l) da matriz
    for c in range(0, 3):  # Itera sobre as colunas (c) da matriz
        # Solicita ao usuário um número e o adiciona à lista na linha l da matriz
        num = int(input(f"Qual o número você quer adicionar à posição {l}, {c}: "))
        matriz[l].append(num)  # Adiciona o número à lista na posição l da matriz

# Loop aninhado para percorrer as linhas e colunas da matriz e imprimir seus elementos
for l in range(0, 3):  # Itera sobre as linhas (l) da matriz
    for c in range(0, 3):  # Itera sobre as colunas (c) da matriz
        # Imprime o elemento da posição l,c entre colchetes e com espaço após
        print(f"[{matriz[l][c]}]", end=" ")
    print()  # Imprime uma nova linha após imprimir todos os elementos de uma linha da matriz
