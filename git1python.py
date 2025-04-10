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
