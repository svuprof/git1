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

class lovelypet:
    def __init__(self,a1,a2):
        self.species = a1
        self.color = a2

    def lovelypet(self):
        print("Pet color is:", self.color)
        print("Pet species is:", self.species)