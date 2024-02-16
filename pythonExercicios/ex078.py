lista = [int(input("Digite o primeiro valor: ")),int(input("Digite o segundo valor: ")),int(input("Digite op terceiro valor: ")),int(input("Digite o quarto valor: ")),int(input("Digite o quinto valor: "))]
print("Essa foi a lista".upper())
print(lista)
contagem = 0
num_menor = 0
num_maior = 0
par_menor = [] # o par quer dizer parametro
par_maior = []
for count,num in enumerate(lista):
    if contagem == 0:
        num_menor = num
        num_maior = num
        par_maior = [count]
        par_menor = [count]
    else:
        if num_menor > num:
            num_menor = num
            par_menor = [count]
        elif num_menor == num:
            par_menor.append(count)
        if num_maior < num:
            num_maior = num
            par_maior = [count]
        elif num_maior == num:
            par_maior.append(count)
    contagem += 1
print(f"O menor número é {num_menor} e está na posição {par_menor}")
print(f"O maior número é {num_maior} e está na posição {par_maior}")
        