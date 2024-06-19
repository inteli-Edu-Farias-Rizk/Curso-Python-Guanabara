class Banco:
    def __init__(self,name,salary):
        self.salary = salary
        # with this two underscores, i make the name private
        self.__name = name
    def show(self):
        print(f'O {self.__name} ganha {self.salary}')
    

Edu = Banco("Edu",4000)
Edu.show()

