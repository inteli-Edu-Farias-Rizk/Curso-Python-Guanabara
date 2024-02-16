emprestimo = int(input("Qual é o valor do empréstimo: "))
salário = int(input("Qual o valor do seu salário? "))
time = int(input("Em quantos anos você pretende pagar: "))

prestaçao = emprestimo/(time*12)

trintasalario = 3/10 * salário

if trintasalario > prestaçao :
    print("Você poderá recerber o empréstimo")
elif trintasalario < prestaçao:
    print("O empréstimo foi negado")