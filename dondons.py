class jesko:
    def __init__(self, tp, hp, cc, trans, tm=False):
        self.topspeed = tp
        self.horsepower = hp
        self.color = cc
        self.transmission = trans
        self.trackmode = tm

    def topspeed(self):
        print(f"Top Speed: {self.topspeed} mph")

    def horsepower(self):
        print(f"Horsepower: {self.horsepower} hp")