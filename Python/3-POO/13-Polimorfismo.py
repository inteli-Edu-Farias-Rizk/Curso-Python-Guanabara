class Phone:
    def __init__(self, brand, model_name, price ) :
        self.brand = brand
        self.model_name = model_name
        self.price = price
    def __str__(self):
        return f"{self.brand}{self.model_name}"
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para o num: {phone_num}")
    def discount(self):
        return self.price*0.1

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price,ram,internal_memory,back_camera):
        super().__init__(brand, model_name, price)


        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
    def discount(self):
        return self.price*0.15
    

Moto = Phone('Moto', 'G7', 3000)
print(Moto)
Moto.make_a_call(232132)
print(f"Valor do {Moto.brand}{Moto.model_name} com desconto é {Moto.price - Moto.discount()}")
print(vars(Moto))


iphone = SmartPhone("Iphone", "13", 5000,"8gb","356gb","25mp")

print(iphone)
iphone.make_a_call()


