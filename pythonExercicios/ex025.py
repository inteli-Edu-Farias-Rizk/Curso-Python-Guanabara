nome = input("Qual é seu nome completo: ").strip()
verfi = "silva" in nome.lower()

if verfi == True :
    print("Seu nome tem Silva")
else:
    print("Seu nome não tem Silva")