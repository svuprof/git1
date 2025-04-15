

class Person:
    def __init__(self, n,g):
        self.name = n
        self.gender = g
        self.children = []

def printname(object):
    print(object.name)

def createlabel(object):
    if object.gender == "f":
        gend = "female"
    else: gend = "male"
    return(f"{object.name} is {gend}")

def showgender(object):
    if object.gender == "f":
        gend = "female"
    else: gend = "male"
    return gend

#gen 1
grandpa = Person("Owen", "m")

#gen 2
dad = Person("Jeremy", "m")
johnny = Person("Johnny", "m")
liz = Person("Liz", "f")
jannie = Person("Jannie", "f")
michelle = Person("Michelle", "f")
rich = Person("Richard", "m")
andrea = Person("Andrea", "f")

#jeremy's kids
me = Person("Ethan","m")
riley = Person("Riley","f")
luke = Person("Luke","m")
jade = Person("Jade","f")
brayden = Person("Brayden","m")
trent = Person("Trent","m")
aubrie = Person("Aubrie","f")



grandpa.children.append(dad)
grandpa.children.append(johnny)
grandpa.children.append(liz)
grandpa.children.append(jannie)
grandpa.children.append(michelle)
grandpa.children.append(rich)
grandpa.children.append(andrea)

dad.children.append(me)
dad.children.append(riley)
dad.children.append(luke)
dad.children.append(jade)
dad.children.append(brayden)
dad.children.append(trent)
dad.children.append(aubrie)

# print(grandpa.name)
# print()
# print(f"{grandpa.name}'s children:")
# list(map(printname, grandpa.children))

# labellist = list(map(createlabel, dad.children))
#
# print(labellist)

def recurse1(person,i,space,parent):
    global males
    global females
    print(f"{space[i-1]}{person.name}, Child of {parent}, Generation {i}")
    if person.gender == "f": females += 1
    elif person.gender == "m": males += 1
    if person.children:
        i += 1
        parent = person.name
        for element in person.children:
            recurse1(element,i,space,parent)
    # return(males,females)
    if person.name == first:
        print()
        print(f"Males in tree: {males}")
        print(f"Females in tree: {females}")

print()

space = ("","    ","        ","          ")
males = 0
females = 0
first = grandpa.name
recurse1(grandpa,1,space,"Wendell")














