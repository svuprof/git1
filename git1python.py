class Person:
  def __init__(self, aa, bb, cc):
    self.name = aa
    self.age = bb
    self.id = cc
    self.street = ""
    self.city = ""
    self.zip = ""
    self.phone = ""

  def myname(self):
      print("Hello my name is " + self.name)

  def myage(self):
      print("Hello my age is " + str(self.age))

  def mynameplusage(self):
      print(self.name +":"+ str(self.age))

class car:
    def __init__(self, aa, bb):
        self.make = aa
        self.model = bb

    def mymake(self):
        print("Make is", self.make)

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