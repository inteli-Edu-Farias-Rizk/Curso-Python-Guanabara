lista = []
count = 0
for c in range (0,5):
    num = int(input("Qual número você gostaria de adicionar: "))
    if c == 0 or lista[-1] < num:
        lista.append(num)
    else:
        count = 0    
        while count < len(lista):
            if lista[count] >= num:
                lista.insert(count,num)
                break
            else:
                count +=1
print(lista)