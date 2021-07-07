#0.
int х
if 5 < х < 10:
    print("Меньше нуля")
else: print("не меньше")
print("дос ивдания");

#1.
my_list = [1, 2, 3, 4, 5]
for _ in range(10):
    func()

#2.
def func_param(p1):
    print("функция с параметром", p1)


my_list = [1, 62, 13, 34, 25]

for element in my_list:
    print("начало цикла")
    func_param(p1=element)

#3.
def power(number, pow):
    print("функция с параметром", number, pow)
    power_value = number ** pow
    return power_value


my_list = [1, 62, 13, 34, 25]

for element in my_list:
    print("начало цикла")
    result = power(number=element, pow=10)
    print(result)

#4.
def create_user():
    name = "Василий"
    age = 21
    return name, age

n, a = create_user()
print(n, a)

#5.
def create_user():
    name = "Василий"
    age = 21
    return name, age

result = create_user()
print(result)

#6.
def multy(n1, n2):
    print("функцию вызвали с параметрами", n1, n2)
    value: int = n1 * n2
    return value
print(multy(42, 27))

#7. проверка типа
def multy(n1, n2):
    print("функцию вызвали с параметрами", n1, n2)
    if isinstance(n1, int):
        value: int = n1 * n2
        return value
    else:
        print("error")
print(multy("42", 27))

#8.
def elefant_found(some_list):
    elefant_in_list = "elefant" in some_list
    if elefant_in_list:
        some_list.remove("elefant")
        print("слон на свободе!!!")
    return elefant_found

zoo = ["monkey", "elefant", "tiger", "mouse", "elefant"]


elefant_found(some_list=zoo)
print(zoo)

elefant_found(some_list=zoo)
print(zoo)

elefant_found(some_list=zoo)
print(zoo)

#9.
import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(100, 100)
sd.circle(center_position=point)

#10.
import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius +=5
    sd.circle(center_position=point, radius=radius, width=2)

#11.
import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


point = sd.get_point(300, 300)
bubble(point=point, step=10)

#12 3 ряда по 10 пузырей
import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step):
    sd.circle(center_position=point)


for y in range(100, 301, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=2)

#13.
my_list = [1,2,3]
for element in my_list:
    print("for", element)
    e, f = int(input()), int(input())

else:
    element = None

print("global element:", element)
print("global e, f:", e, f)

#14. Вывести треугольник
b = "*"
a = 1
while a<=5:
    print(a*b)
    a += 1


#15.
genome = input()
bnt=0
for cunt in genome:
    if cunt == "o":
        bnt += 1
print(bnt)