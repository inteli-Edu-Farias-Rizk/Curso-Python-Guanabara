data = 2023
data_nasc = int(input("Qual a seu ano de nascimento: "))

idade = data - data_nasc

if idade < 18:
    print("Não é nescessário o alistamento")
elif idade > 18 :
    print("Já passou do dia de fazer o alistamento, Faça imediatamente")
else:
    print("Agora é o ano para se fazer o alistamento")