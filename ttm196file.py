class game:
    def __init__(self, a, b, c):
        self.location = a
        self.date = b
        self.time = c
        self.home_team = ''
        self.away_team = ''
        self.home_score = 0
        self.away_score = 0
        self.time_remaining = 60
        self.period = 3

    def start(self):
        print(self.away_team.name,'@', self.home_team.name,': game start')
    def end(self):
        print(self.away_team.name,'@', self.home_team.name,': end of game')
    def show_score(self):
        print(self.home_team.name,'score =',self.home_score,' | ',self.away_team.name,'score =',self.away_score)

#====================================================================================

class team:
    def __init__(self, a, b, c, d):
        self.name = a
        self.coach = b
        self.mascot = c
        self.sport = d
        self.players = []

    def win(self):
        print(self.name,'wins!')
    def lose(self):
        print(self.name,'lost!')
    def teampenaltykill(self):
        print(self.name,'kills off a penalty')
    def powerplay(self):
        print(self.name,'are on the power play')
    def possession(self):
        print(self.name,'GAIN POSSESSION')

#====================================================================================

class Person:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.gender = c
    def myself(self):
        print(f'Name:{self.name},age:{self.age},gender:{self.gender}')

#====================================================================================

class Athlete(Person):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.sport = d

#====================================================================================

class HockeyPlayer(Athlete):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, 'Hockey')
        self.position = d
    def show(self):
        print(f'Hockey player traits={self.name},{self.sport},{self.position}')
    def details(self):
        super().details()
        print(f'position={self.position}')
        print('position'+str(self.position))

    def goal(self):
        print(self.name,'SCORES!')
    def save(self):
        print(self.name,'makes a save')
    def passes(self):
        print(self.name,'passes the puck')
    def receive(self):
        print(self.name,'receives the puck')
    def shoot(self):
        print(self.name,'shoots the puck')
    def icing(self):
        print(self.name,'ices the puck')
    def faceoff(self):
        print(self.name,'wins the faceoff')
    def interference(self):
        print(self.name,'receives a minor penalty for interference')
    def tripping(self):
        print(self.name,'receives a minor penalty for tripping')
    def holding(self):
        print(self.name,'receives a minor penalty for holding')
    def hooking(self):
        print(self.name,'receives a minor penalty for hooking')
    def roughing(self):
        print(self.name,'receives a minor penalty for roughing')
    def fighting(self):
        print(self.name,'receives a 5-minute major for fighting')
    def fight(self):
        print(self.name,'drops the gloves for a fight')
    def playerpenaltykill(self):
        print(self.name,'is out of the penalty box')
    def offside(self):
        print(self.name,'is offside')
    def hit(self):
        print(self.name,'lands a hit')
    def move(self):
        print(self.name,'moves up the ice')
    def poke(self):
        print(self.name,'pokes the puck away')
    def intercept(self):
        print(self.name,'intercepts the puck to gain possession')
    def steal(self):
        print(self.name,'steals the puck')

#====================================================================================

canes = team('Carolina Hurricanes','Brindamor','Stormy','hockey')
rags = team('New York Rangers','Laviolette','N/A','hockey')

#====================================================================================

seth = HockeyPlayer('Seth Jarvis','23','M','LW')
sebastian = HockeyPlayer('Sebastian Aho','27','M','C')
jackson = HockeyPlayer('Jackson Blake','21','M','RW')
jaccob = HockeyPlayer('Jaccob Slavin','30','M','D')
brent = HockeyPlayer('Brent Burns','40','M','D')
pyotr = HockeyPlayer('Pyotr Kochetkov','25','M','G')

canes.players.append(seth)
canes.players.append(sebastian)
canes.players.append(jackson)
canes.players.append(jaccob)
canes.players.append(brent)
canes.players.append(pyotr)

print(canes.name,'LINEUP')
print('––',canes.players[0].name,'as left winger','––')
print('––',canes.players[1].name,'as center forward','––')
print('––',canes.players[2].name,'as right winger','––')
print('––',canes.players[3].name,'as defenseman','––')
print('––',canes.players[4].name,'as defenseman','––')
print('––',canes.players[5].name,'as goaltender','––')

#====================================================================================

panarin = HockeyPlayer('Artemi Panarin','33','M','LW')
trocheck = HockeyPlayer('Vincent Trocheck','31','M','C')
othmann = HockeyPlayer('Brennan Othmann', '22', 'M', 'RW')
soucy = HockeyPlayer('Carson Soucy', '30', 'M', 'D')
fox = HockeyPlayer('Adam Fox', '27', 'M', 'D')
igor = HockeyPlayer('Igor Shesterkin', '29', 'M', 'G')

rags.players.append(panarin)
rags.players.append(trocheck)
rags.players.append(othmann)
rags.players.append(soucy)
rags.players.append(fox)
rags.players.append(igor)

print(rags.name,'LINEUP')
print('––',rags.players[0].name,'as left winger','––')
print('––',rags.players[1].name,'as center forward','––')
print('––',rags.players[2].name,'as right winger','––')
print('––',rags.players[3].name,'as defenseman','––')
print('––',rags.players[4].name,'as defenseman','––')
print('––',rags.players[5].name,'as goaltender','––')

#====================================================================================

match1=game('canes','2025/04/07','7:00')
match1.home_team =canes
match1.away_team=rags
print('')
match1.start()
match1.time_remaining=0
print('')
print('–– 1ST PERIOD START ––')
sebastian.faceoff()
canes.possession()
brent.receive()
brent.passes()
seth.receive()
seth.move()
trocheck.hit()
panarin.steal()
rags.possession()
panarin.move()
panarin.passes()
othmann.receive()
othmann.shoot()
pyotr.save()
jaccob.receive()
canes.possession()
jaccob.passes()
jackson.receive()
soucy.poke()
soucy.tripping()
canes.powerplay()
sebastian.faceoff()
jaccob.receive()
jaccob.shoot()
igor.save()
seth.move()
seth.goal()
match1.home_score+=1
match1.time_remaining=40
match1.show_score()
print('–– END OF 1ST PERIOD ––')
print('')
print('–– 2ND PERIOD START ––')
trocheck.faceoff()
rags.possession()
fox.receive()
panarin.move()
fox.passes()
panarin.receive()
panarin.shoot()
panarin.goal()
match1.away_score+=1
match1.time_remaining=30
match1.show_score()
trocheck.faceoff()
rags.possession()
soucy.receive()
soucy.passes()
jackson.intercept()
canes.possession()
jackson.move()
jackson.passes()
fox.hit()
seth.fight()
seth.fighting()
fox.fighting()
print('–– END OF 2ND PERIOD ––')
print('')
print('–– 3RD PERIOD START ––')
trocheck.faceoff()
rags.possession()
soucy.receive()
othmann.move()
soucy.passes()
othmann.receive()
othmann.shoot()
pyotr.save()
panarin.receive()
brent.hit()
canes.possession()
brent.passes()
sebastian.receive()
sebastian.offside()
sebastian.faceoff()
canes.possession()
jackson.receive()
jackson.shoot()
jackson.goal()
match1.home_score+=1
match1.time_remaining=0
print('–– END OF 3RD PERIOD ––')
match1.end()
print('')
match1.show_score()