def notas(*d, sit=False):
    maior = menor = 0
    total = 0
    media = 0
    dic = {}
    for i in d:
        media += i
        if total == 0:
            menor = i 
            maior = i 
        else:
            if menor > i:
                menor = i
            if i > maior:
                maior = i
        total += 1

    
    dic['media'] = media/total
    dic['maior'] = maior
    dic['menor']= menor
    dic['total'] = total
    return dic
resp = notas(5.5,9.5,10,6.5, sit=True)
print(resp)
        
        