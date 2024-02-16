from random import randint
n = ((randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)))

print(f"Eu sorteei os valores {n}")

#mais bonito seria desse modo 
print(f"Os valores sorteados foram: ")
for c in n:
    print(f"{c} ",end ='')


