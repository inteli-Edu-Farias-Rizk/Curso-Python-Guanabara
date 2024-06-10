class Movie:
    #This is the method contructor
    def __init__(self,name, yearLaunch,includedPlan,note,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan=includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    #this is for when you print the object you control what it gives 
    def __str__(self):
        return f'Filme: {self.name}'
    def technical_sheet(self):
        print(f"O nome do filme é {self.name} e o seu ano de lançamento é {self.yearLaunch}")
    
mario = Movie("Super Mario", 2020, False, 10,2000)
mario.technical_sheet()