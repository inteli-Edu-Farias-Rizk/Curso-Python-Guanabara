n1 = float(input("Qual é a sua primeira nota: "))
n2 = float(input("Qual é a sua segunda nota: "))

media = (n1 + n2)/2
print("A sua media foi {}".format(media))
if media < 5:
    print("Reprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
elif media > 7:
    print("Aprovado")