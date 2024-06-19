"""
1 - O método de classe utliza o primeiro parâmetro cls referente a classe
2 - O método de classe pode acessar ou modificar o estado da classe 
3 - Usamos o decorator @classmethod em python para criar um método de classe
""" 
class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def fromText(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        #aqui ele está passando os parametros para o própio constructor
        return cls(name, int(price))
    

Wiuu = Console.fromText("Meu console é Wiu e o preço dele é 1000 reais")
xboxOne = Console.fromText("Meu console é Xbox e o preço é 2000 reais")
# This will transform the object into a dictionarie
print(Wiuu.__dict__)
print()
