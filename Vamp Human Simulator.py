import random
import matplotlib.pyplot as plt
import sys

XMAX = 1000
YMAX = 1000

randX = random.randint(0, XMAX)
randY = random.randint(0, YMAX)

if (len(sys.argv) < 4):
    print('argv too short, usage: python3 <init_humanpop> <init_vamppop> <timesteps>')
    print('Using default values for initial human pop (20), initial vampire pop (20), timesteps (80)')
    init_humanpop = 20 
    init_vamppop = 20
    timesteps = 80
else:
    init_humanpop = int(sys.argv[1])
    init_vamppop = int(sys.argv[2])
    timesteps = int(sys.argv[3])

class Human():
    health = 100
    age = random.randint(10, 50)
    pos = [randX, randY]
    mapsize = [XMAX, YMAX]

    def __init__(self, health, age, pos, mapsize):
        self.health = health
        self.age = age
        self.pos = pos
        self.mapsize = mapsize

    def move(self):
        steps = random.randint(-4, 4)
        self.health -= 1 * abs(steps)
        self.age += 1 * abs(steps)
        self.pos[0] += steps
        self.pos[1] += steps

        if (self.age == self.age + 70):
            steps = 0
            self.pos[0] += 0
            self.pos[1] += 0

        if self.pos[0] < 0:
            self.pos[0] = 0

        elif self.pos[0] >= self.mapsize[0]:
            self.pos[0] = self.mapsize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0

        elif self.pos[1] >= self.mapsize[1]:
            self.pos[1] = self.mapsize[1]

class Vampire(Human):
    pos = [randX, randY]
    mapsize = [XMAX, YMAX]
    
    def __init__(self, health, pos, mapsize):
        self.health = health
        self.pos = pos
        self.mapsize = mapsize

    def bite(self):
        Damage = random.randint(1, 5)
        self.health -= Damage

    def move(self):
        steps = random.randint(-8, 8)
        self.pos[0] += steps
        self.pos[1] += steps

        if self.pos[0] < 0:
            self.pos[0] = 0

        elif self.pos[0] >= self.mapsize[0]:
            self.pos[0] = self.mapsize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0

        elif self.pos[1] >= self.mapsize[1]:
            self.pos[1] = self.mapsize[1]

class Water():
    
    name = "Water"
    healthpoints = 50
    pos = [randX, randY]

    def __init__(self, name, size, color, healthpoints, pos, mapsize):
        self.name = name
        self.size = size
        self.color = color
        self.healthpoints = healthpoints
        self.pos = pos
        self.mapsize = mapsize

class Food():

    name = "Food"
    healthpoints = 30
    pos = [randX, randY]

    def __init__(self, name, size, color, healthpoints, pos, mapsize):
        self.name = name
        self.size = size
        self.color = color
        self.healthpoints = healthpoints
        self.pos = pos
        self.mapsize = mapsize

class Garlic():

    name = "Garlic"
    healthpoints = 100
    pos = [randX, randY]

    def __init__(self, name, size, color, healthpoints, pos, mapsize):
        self.name = name
        self.size = size
        self.color = color
        self.healthpoints = healthpoints
        self.pos = pos
        self.mapsize = mapsize

chance = random.uniform(0.01, 1.00)

def killed_by_human(VampireList, HumanList):
    for vampire in VampireList:
        for human in HumanList:
            if (human.pos[0] == vampire.pos[0]):
                if (human.pos[1] == vampire.pos[1]):
                    if (chance < 0.30):
                        for vampire in VampireList:
                            vampire.health = 0
                            VampireList.remove(vampire)
                                #The vampire has a 30% chance of being killed by the human. 
                    else:
                        vampire2 = bitten(human)
                        VampireList.append(vampire2)
                        HumanList.remove(human)

def bites_each_other(VampireList):
    for vampire1 in VampireList:
        for vampire2 in VampireList:
            if (vampire1.pos[0] == vampire2.pos[0]):
                if (vampire1.pos[1] == vampire2.pos[1]):
                    Damage = int(20)
                    bite_chance = random.uniform(0.01, 1.00)
                    if (bite_chance < 0.50):
                        vampire1.health -= Damage
                        if (vampire1.health == 0):
                            VampireList.remove(vampire1)
                    else:
                        vampire2.health -= Damage
                        if (vampire2.health == 0):
                            VampireList.remove(vampire2)

def selfish(HumanList):
    for human1 in HumanList:
        for human2 in HumanList:
            if (human1.pos[0] == human2.pos[0]):
                if (human1.pos[1] == human2.pos[1]):
                    if(chance < 0.40):
                        selfish_chance = random.uniform(0.01, 1.00)
                        if (selfish_chance < 0.50):
                            human1.health += 20
                            human2.health -=20
                            if (human1.health == 0):
                                HumanList.remove(human1)
                        else:
                            human1.health -= 20
                            human2.health +=20
                            if (human2.health == 0):
                                HumanList.remove(human2)

def help(HumanList):
    for human1 in HumanList:
        for human2 in HumanList:
            if(chance > 0.40):
                human1.health += 10
                human2.health +=20
        
def drinkWater(HumanList, WaterList):
    for human in HumanList:
        for water in WaterList:
            if (human.pos == water.pos):
                human.health += 50

def eatfood(HumanList, FoodList):
    for human in HumanList:
        for food in FoodList:
            if (human.pos == food.pos):
                human.health += 30

def eatgarlic(HumanList, GarlicList):
    for human in HumanList:
        for garlic in GarlicList:
            if (human.pos == garlic.pos):
                human.health += 100

def bitten(human):
    if(Human.pos == Vampire.pos):
        if (chance > 0.30):
            vampire = Vampire(Human.health, Human.pos, Vampire.mapsize)
        return vampire

def main():
        HumanList = []
        VampireList = []
        WaterList = []
        FoodList = []
        GarlicList = []

        for i in range(init_humanpop):
            randX = random.randint(0, XMAX)
            randY = random.randint(0, YMAX)
            HumanList.append(Human(Human.health, Human.age, [randX, randY], [XMAX, YMAX]))
        for i in range(init_vamppop):
            randX = random.randint(0, XMAX)
            randY = random.randint(0, YMAX)
            VampireList.append(Vampire(Human.health, [randX, randY], [XMAX, YMAX]))
               
            WaterList.append(Water(Water.name, 30, "blue", Water.healthpoints, [randX, randY], [XMAX, YMAX]))
            FoodList.append(Food(Food.name, 30, "brown", Food.healthpoints, [randX, randY], [XMAX, YMAX]))
            GarlicList.append(Garlic(Garlic.name, 50, "gray", Garlic.healthpoints, [randX, randY], [XMAX, YMAX]))

        for i in range(timesteps):
            print("\n ### TIMESTEP ",i, "###")
            print("Human: {0}  Vampire: {1}".format(len(HumanList), len(VampireList)))
            xvalues_human = []
            yvalues_human = []

            xvalues_vampire = []
            yvalues_vampire = []

            xvalues_water = []
            yvalues_water = []

            xvalues_food = []
            yvalues_food = []

            xvalues_garlic = []
            yvalues_garlic = []

            for human in HumanList:
                human.move()
                xvalues_human.append(human.pos[0])
                yvalues_human.append(human.pos[1])

                if (i == 70):
                    HumanList.clear()

            for vampire in VampireList:
                vampire.move()
                xvalues_vampire.append(vampire.pos[0])
                yvalues_vampire.append(vampire.pos[1])

                if(vampire.health == 0):
                    VampireList.remove(vampire)

            for water in WaterList:
                xvalues_water.append(water.pos[0])
                yvalues_water.append(water.pos[1])

            for food in FoodList:
                xvalues_food.append(food.pos[0])
                yvalues_food.append(food.pos[1])

            for garlic in GarlicList:
                xvalues_garlic.append(garlic.pos[0])
                yvalues_garlic.append(garlic.pos[1])

            killed_by_human(VampireList, HumanList)
            drinkWater(HumanList, WaterList)
            eatfood(HumanList, FoodList)
            eatgarlic(HumanList, GarlicList)
            selfish(HumanList)
            help(HumanList)
            bites_each_other(VampireList)

            plt.scatter(xvalues_human, yvalues_human, s = 50, c="green", marker="o")
            plt.scatter(xvalues_vampire, yvalues_vampire, s = 80, c="red", marker="o")   
            plt.scatter(xvalues_water, yvalues_water, s = 30, c="blue", marker="o")
            plt.scatter(xvalues_food, yvalues_food, s = 30, c="brown", marker="o") 
            plt.scatter(xvalues_garlic, yvalues_garlic, s = 50, c="grey", marker = "^")
            plt.xlim(0,XMAX)
            plt.ylim(0,YMAX)
            plt.pause(1)
            plt.clf()

        if (i == timesteps):
            plt.gcf()
            plt.savefig("humanvampire.png")

if __name__ == "__main__":
    main()