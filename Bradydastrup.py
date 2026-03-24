class Person:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.gender = c
    def myself(self):
        print(f"Name: {self.name} age: {self.age} gender: {self.gender}")


class Athlete(Person):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.sport = d

    class SoccerPlayer(Athlete):
        def __init__(self, a, b, c, d, e):
            super().__init__(a, b, c, "Soccer")
            self.shotacc = d
            self.cleat = e

        def Soccertrait(self):
            print(f'Their shot accuracy: {self.shotacc}%')

        def Soccershoe(self):
            print(f'Favorite type of cleat: {self.cleat}')