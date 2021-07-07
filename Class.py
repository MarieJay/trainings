#1.
class Toyota:
    def __init__(self):
        self.color = "Бордовый металик"
        self.price = "1 000 000 руб"
        self.max_velocity = "200 км/час"
        self.current_velocity = "0 км/час"
        self.engine_rpm = 0

    def start(self):
        print("Мотор запущен")
        self.engine_rpm = 900

    def go(self):
        print("Поехали!")
        self.engine_rpm = 2000
        self.current_velocity = "20 км/час"


My_car = Toyota()
print("color", My_car.color)
print("price", My_car.price)
print("max_velocity", My_car.max_velocity)
print("current_velocity", My_car.current_velocity)
print("rpm", My_car.engine_rpm)

My_car.start()
print("rpm", My_car.engine_rpm)
My_car.go()
print("rpm", My_car.engine_rpm)
print("current_velocity", My_car.current_velocity)

produced, plan = 0, 10000
warehouse = []
while produced < plan:
    new_car = Toyota()
    warehouse.append(new_car)
    produced +=1

#2.
class Robot:
    def __init__(self):
        self.name = "R2D2"

    def hello(self):
        print("Hello, World! I am {}".self.name)


#3.
class Robot:
    def __init__(self):
        self.name = "R2D2"

    def hello(self):
        print("Hello, World! I am", self.name)

my_robot = Robot()
my_robot.hello()

my_robot.temperature = 1

while my_robot.temperature <10:
    my_robot.temperature *=2
print((my_robot.temperature))

del my_robot.temperature #удаляет перемнную ссылку из простнаства имен
print((my_robot.temperature))


#4.
class Backpack:
    def add(self, item):
        print("в рюкзак положили", item)
        self.content = item


my_backpack = Backpack()
my_backpack.add(item = "ноутбук") #вызвали через класс и передали указать на сайт,
# когда обращаемся через класс, мы должны указывать

my_mom_backpack = Backpack()
my_mom_backpack.add(item = "ланч")

print(my_backpack.content)

print(Backpack.add)
print(my_backpack.add)

my_backpack.add(item = "iphone")
Backpack.add(self= my_mom_backpack, item = "мамин iphone")

#5.
class Backpack:
    def __init__(self): #вызывается чтобы завести перемнные, которые ему нужны для жизни
        self.content = []

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def inspect(self):
        print("В рукзаке лежит:")
        for item in self.content:
            print(item)


My_backpack = Backpack()
My_backpack.add(item = "ноутбук")
My_backpack.add(item = "зарядка")
My_backpack.inspect()


#7.

class Backpack:
    def __init__(self, gift = None): #вызывается чтобы завести перемнные, которые ему нужны для жизни
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def inspect(self):
        print("В рукзаке лежит:")
        for item in self.content:
            print("    ",item)

    def __del__(self):
        self.content = None
        print("прощай мир...")


My_backpack = Backpack(gift="флешка")
My_backpack.add(item = "ноутбук")
My_backpack.add(item = "зарядка")
My_backpack.inspect()

var1 = Backpack(gift="флешка")
var1 = None
My_backpack = None

#8.
class Backpack:
    def __init__(self, gift = None): #вызывается чтобы завести перемнные, которые ему нужны для жизни
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def __str__(self):
        return "Backpack: " + ", ".join(self.content)

My_backpack = Backpack(gift="флешка")
My_backpack.add(item = "ноутбук")
My_backpack.add(item = "зарядка")

print(My_backpack)

#9.
class Backpack:
    def __init__(self, gift = None): #вызывается чтобы завести перемнные, которые ему нужны для жизни
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def __str__(self):
        return "Backpack: " + ", ".join(self.content)

#    def __bool__(self):
#        return self.content != []

    def __len__(self):
        return len(self.content)

My_backpack = Backpack()

print(bool(My_backpack), len(My_backpack))
print(My_backpack)

#10.
class Backpack:
    def __init__(self, gift = None): #вызывается чтобы завести перемнные, которые ему нужны для жизни
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def __str__(self):
        return "Backpack: " + ", ".join(self.content)

    def __bool__(self):
        return self.content != []

#    def __len__(self):
#        return len(self.content)

My_backpack = Backpack()

if My_backpack:
    print("рюзкзак не пустой")
#    print(len(My_backpack))
else: print("рюкзак пустой")

#11.
from random import randint


class lemming:
    pass

total_lemmings = 0

lemming_1 = lemming()
total_lemmings +=1
lemming_2 = lemming()
total_lemmings +=1
lemming_3 = lemming()
total_lemmings +=1

family = []
family_size = randint(16, 32)
while len(family) < family_size:
    new_lemming = lemming()
    family.append(new_lemming)
    total_lemmings +=1
print(total_lemmings)

#12.
from random import randint


class lemming:
    total = 0

    def __init__(self):
        lemming.total +=1

burrow = []
burrow_depth = randint(90, 100)
while len(burrow) < burrow_depth:
    family = []
    family_size = randint(16, 32)
    while len(family) < family_size:
        new_lemming = lemming()
        family.append(new_lemming)
    burrow.s(family)
print(lemming.total)

#13.
from random import randint, choice


class lemming:
    total, names = 0, ["Marie", "Castiel", "Dean Winchester", "Jayfeather", "Leafpool", ]
    names_count = len(names)
    some_text = "На балл пойдет "
    some_var = some_text + names[-1]

    def __init__(self):
        lemming.total +=1
        self.name = choice(lemming.names) #выбирает случайное из списка

    def __str__(self):
        return "lemming" + self.name

    def check_class_attr(self):
        print("lemmings.total", lemming.total)
        print("lemmings.names", lemming.names)
        print("lemmings.names_count", lemming.names_count)
        print("lemmings.some_text", lemming.some_text)
        print("lemmings.some_var", lemming.some_var)


new_lemming = lemming()
print("lemmings.total", lemming.total)
print("lemmings.names", lemming.names)
print("lemmings.names_count", lemming.names_count)
print("lemmings.some_text", lemming.some_text)
print("lemmings.some_var", lemming.some_var)
new_lemming.check_class_attr()

#14.
from random import random


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay*= (1.0+percent)

workwr_1 = Worker("Castiel Winchester", "1 trln")
print(workwr_1.lastName())

w = random()
print(w)

#15.
from random import randint, choice


class lemming:
    tail = 20
    total = 0
    def __init__(self):
        self.name = choice(["Cas", "Dean", "Sam"])
        self.tail = randint(15, 25)
        lemming.total = lemming.total + 1

    def __str__(self):
        return  "Lemming " + self.name + " with a tail length " + str(self.tail)


print(lemming.tail)
new_rat = lemming()
print(new_rat.tail)
print(new_rat)
