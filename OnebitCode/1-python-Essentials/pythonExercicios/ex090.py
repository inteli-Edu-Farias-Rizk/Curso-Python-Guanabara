dic = {}
nomeDele = input("Qual o nome do aluno: ")
dic["nome"] = nomeDele
media  = float(input("Qual a media do aluno: "))
dic["media"] = media
for c,v in dic.items():
    print(f"A {c} dele é {v}")

if dic["media"] < 6:
    print("Reprovado")
else:
    print("Aprovado")