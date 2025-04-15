import time

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
        print(f"The max speed of the {self.model} is {self.maxspeed}")

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

class lovelypet:
    def __init__(self,a1,a2):
        self.species = a1
        self.color = a2

    def lovelypet(self):
        print("Pet color is:", self.color)
        print("Pet species is:", self.species)

class Videogame:
    def __init__(self, studio, name, ip, year, genre, size, version):
        self.studio = studio,
        self.name = name,
        self.year = year,
        self.genre = genre,
        self.size = size,
        self.ip = ip,
        self.version = version
    def info(self):
        print(f'{self.name}\n Studio: {self.studio}\nIP: {self.ip}\nGame info:\nYear: {self.year}\nGenre: {self.genre}\nSize: {self.size}')
    def run_game(self):
        print(f'Loading game...')
        time.sleep(1)
        print(f'{self.name} Version {self.version}')
        time.sleep(0.1)
        print(f'Now loading...')
        time.sleep(1)
        print(f'{self.name}\nPress any key to start!')

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

class rugby:
    def __init__(self, first, last, version, position, height, weight, bronco):
        self.first = first
        self.last = last
        self.version = version
        self.position = position
        self.height = height
        self.weight = weight
        self.bronco = bronco

    def version(self):
        print("I play", self.version)

    def size(self):
        print("I am ", self.height, self.weight)
class ElectricCar:
    def __init__(self, brand, model, battery_kwh, range_miles, has_autopilot):
        self.brand = brand
        self.model = model
        self.battery_kwh = battery_kwh
        self.range_miles = range_miles
        self.has_autopilot = has_autopilot

    def display_specs(self):
        print(f"{self.brand} {self.model} | Battery: {self.battery_kwh}kWh | Range: {self.range_miles} miles")
        if self.has_autopilot:
            print("This car has autopilot.")
        else:
            print("This car does not have autopilot.")

    def charge_status(self):
        print(f"Charging {self.brand} {self.model}...")
        print(f"Estimated full charge range: {self.range_miles} miles with a {self.battery_kwh}kWh battery.")
