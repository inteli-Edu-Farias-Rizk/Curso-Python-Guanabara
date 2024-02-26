def leiaInt(frase):
    while True:
        num = input(frase)
        if num.strip().isnumeric():
            return int(num)
        else:
            print('Erro! Digite um numero válido')
    

n = leiaInt('Digite um numero: ')
print(f"Você acabou de digitar o número {n} ")