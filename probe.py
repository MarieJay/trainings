from random import randint
from termcolor import cprint

class man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self): #когда пытаемся вывести на консоль
        return "Я - {}, моя сытость {}".format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >10:
            cprint("{} поел".format(self.name), "green")
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint("{} не поел".format(self.name), "red")
            self.fullness -= 10

    def shopping(self):
        if self.house.money >=50:
            cprint("{} сходил в магазин за едой".format(self.name), color="green")
            self.house.money -= 50
            self.house.food += 30
            self.eat()
        else:
            cprint("{} не хватило денег".format(self.name), "red")

    def work(self):
        cprint("{} сходил на работу".format(self.name), color = "green")
        self.house.money += 50
        self.fullness -= 10

    def watch_TV(self):
        cprint("{} весь день смотрел телевизор".format(self.name), "magenta")
        self.fullness -= 10

    def act(self):
        if self.fullness < 0:
            cprint("{} умер".format(self.name), "red")
            return
        dice = randint(1, 6)
        cprint("на кубике выпало: {}".format(dice), color="grey")
        if self.fullness < 40:
            self.eat()
            # if self.name != "Кенни":
        elif self.house.food < 30:
           self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        else:
            self.watch_TV()

    def enter_the_house(self, house):
        self.house = house
        self.fullness -=10
        cprint("{} въехал в дом".format(self.name), "cyan")


class house:
    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return "В доме еды осталось {} хлопьев, а денег ${}".format(
            self.food, self.money)


My_sweet_home = house()
citizens = [man(name ="Бивис"), man(name ="Батхед"), man(name ="Кенни")]
for citizen in citizens:
    citizen.enter_the_house(house=My_sweet_home)


for day in range(1, 21):
    cprint("================ день {} =================".format(day), color = "yellow")
    for citizen in citizens:
        citizen.act()
    for citizen in citizens:
        print(citizen)

    print(My_sweet_home)
