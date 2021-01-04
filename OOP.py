class Person():
    def __init__(self, name):
        self.name = name
    
    def Reveal(self):
        print("Hi, my name is {}".format(self.name))

class SuperHero(Person):
    def __init__(self, name , hero_name):
         super().__init__(name)
         self.hero_name = hero_name
    
    def Reveal(self):
        super().Reveal()
        print("...And I am {}".format(self.hero_name))

dp = SuperHero('Wade Wilson', 'Deadpool')
dp.Reveal()