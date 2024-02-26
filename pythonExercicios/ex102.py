def fatorial(num, show=False):
    cont = 1
    steps = []  # To store the steps if show is True
    for c in range(num, 0, -1):
        cont *= c
        if show:
            steps.append(str(c))
    if show:
        # Join the steps with ' x ' and add ' = ' and the result at the end
        return ' x '.join(steps) + ' = ' + str(cont) # a função join pe muito util para juntar os elementos de um array, mas precisa ser um array de strings para funcionar
    else:
        return cont

r1 = fatorial(5, show=True)
print(r1)