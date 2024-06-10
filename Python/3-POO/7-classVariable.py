class Movie:
    # the class variable is defined out of the constructor, so that is common to all objects of the class
    platform = 'Netflixs'

    # This is the constructor method
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = []
        self.numAv = 0
        self.durationMinutes = durationMinutes
    
    # This controls what is returned when the object is printed
    def __str__(self):
        return f'Filme: {self.name}'
    
    def technical_sheet(self):
        print(f"O nome do filme é {self.name} e o seu ano de lançamento é {self.yearLaunch}")
    
    def Avaliadores(self):
        while True:
            nota = int(input("Qual a nota que você dá para o filme? "))
            self.note.append(nota)
            self.numAv += 1
            decisao = int(input("Você deseja continuar? [1] Sim [2] Não: "))
            if decisao == 2:
                break
    
    def Media(self):
        if len(self.note) == 0:
            return 0
        soma = sum(self.note)
        media = soma / len(self.note)
        return media

mario = Movie('SuperMario', 2020, False, 200)
mario.Avaliadores()
print(f"A nota média dos filmes foi {mario.Media()} e o total de avaliações foi {mario.numAv}")

#modificando a variavel de classe
Movie.platform = "Amazon"
#A partir de aqui para baixo a variavel de classe vai estar mudada  
