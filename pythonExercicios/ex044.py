preço = int(input("Qual o preço do valor do produto que deseja consumir: "))
fpag = int(input("Qual vai ser a forma de pagamento? 1-dinheiro 2-cartão: "))
juros = preço * 2/10 + preço
valordin = preço * 9/10
if fpag == 1:
    print("O valor a ser pago é {:.0f} reais".format(valordin))
else:
    cartao = int(input("Qantos vezes será parcelado? "))
    if cartao == 1:
        print("O valor a ser pago é {} reais".format(preço * 95/100))
    elif cartao == 2 :
        print("O preço a ser pago é {} reais".format(preço))
    else:
        print("O preço será {:.0f} reais".format(juros))
        print("Cada parcela será de {} ".format(juros/cartao))