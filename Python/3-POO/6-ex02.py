class Product:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco 
    def __str__(self):
        return f'Esse é o produto {self.nome}'
    def discount(self,dis):
        final = self.preco * (dis/100)
        self.preco = final
        return self.preco
    
carro = Product('MegaBlaster', 50)
print(f"O preco é {carro.preco}")
final = carro.discount(20)
print(f"Agora é {final}")
