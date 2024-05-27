from datetime import datetime
def voto(ano):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - ano
    print(f"Com {idade} : ", end ='')
    if idade >= 18 and idade < 65:
        return 'VOTO OBRIGATORIO'
    elif idade < 18:
        return 'NEGADO'
    else:
        return 'VOTO OPCIONAL'
r1 = voto(int(input("Em que ano você nasceu: ")))

print(r1)