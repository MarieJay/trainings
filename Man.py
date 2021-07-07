from random import randint
from termcolor import cprint

class man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 40
        self.money = 0

    def __str__(self): #когда пытаемся вывести на консоль
        return "Я - {}, моя сытость {}, еды осталось {}, денег {}".format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >10:
            print("{} поел".format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print("{} не поел".format(self.name))

    def shopping(self):
        if self.money >=50:
            print("{} сходил в магазин за едой".format(self.name))
            self.money -= 50
            self.food += 30
            self.eat()
        else:
            print("{} не хватило денег".format(self.name))

    def work(self):
        cprint("{} сходил на работу".format(self.name), color = "green")
        self.money += 50
        self.fullness -= 10

    def play_Dota(self):
        cprint("{} весь день играл в доту".format(self.name), "magenta")
        self.fullness -= 10

    def act(self):
        if self.fullness < 0:
            cprint("{} умер".format(self.name), "red")
            return
        dice = randint(1, 6)
        cprint("на кубике выпало: {}".format(dice), color="grey")
        if self.fullness < 40:
            self.eat()
        elif self.food < 30:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        else:
            self.play_Dota()

Vasya = man(name ="Вася")
for day in range(1, 1021):
    cprint("================ день {} =================".format(day), color = "yellow")
    Vasya.act()
    print(Vasya)
# print(Vasya)
# Vasya.eat()
# Vasya.work()
# print(Vasya)
# Vasya.play_Dota()
# print(Vasya)
