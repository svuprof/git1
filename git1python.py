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

class Script:
    def __init__(self, sn, og, ln, ty):
        self.scriptname = sn
        self.origin = og
        self.language = ln
        self.type = ty
        self.details = ""

    def myscriptname(self):
        print("My favorite script is " + self.scriptname + ".")

    def myorigin(self):
        print("It's from " + self.origin +".")

    def mylanguage(self):
        print("It is used for the " + self.language + " language.")

    def mytype(self):
        print("It is a " + self.type + " script.")