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
movie = Movie('One piece',2001,False,5.0,130)
print(movie.name)