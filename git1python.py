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
    def __init__(self, aa, bb, cc):
        self.make = aa
        self.model = bb
        self.maxspeed = cc

    def mymake(self):
        print(f"Make is {self.make}")

    def myspeed(self):
        print(f"The max speed of the {self.model} is {self.speed}")



