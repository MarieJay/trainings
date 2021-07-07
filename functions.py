#1. Локальные переменные
a, b = 1, 2


def simple():
    a = 2
    print("local", a + b)


print("global", a + b)
simple()


#2. Параметры
def vector(x, y, z):
    return x ** 2 + y * z


res = vector(6, 2, 3)
print(res)
#3. Распаковка
def vector_module(x, y, z):
    return x**2 + y*z


some_list = [4, 2, 3]
some_list = [4, 2, 3, 1]
res = vector_module(x=some_list[0], y=some_list[1], z=some_list[2])
print(res)

#3.
def process(subject, action="мыла", object="раму"):
    print(subject)
    print(action, object)


process(subject = "папа", action= "мыл")
process(subject = "брат", action= "мыл")

#4. Добавление элемента
def add_element(element, list_to_add):
    list_to_add.append(element)
    return list_to_add

my_list = [1, 2, 3]
add_element(element=5, list_to_add=my_list)
print(my_list)

#5.
def add_element(element, list_to_add=[]):
    list_to_add.append(element)
    return list_to_add

my_list = add_element(element=5)
print(my_list)

my_list = add_element(element=7, list_to_add=my_list)
print(my_list)

#6. Добавление в разные списки
def add_element(eement, list_to_add=None):
    if list_to_add is None:
        list_to_add=[]
    list_to_add.append(eement)
    return list_to_add

my_list = add_element(eement=5)
print(my_list)

my_list = add_element(eement=7, list_to_add=my_list)
print(my_list)

another_list = add_element(eement=9)
print(another_list)


#7. tuple - неизменяемый список
def print_Them_all(*args):
    print("bla bla bla")
    print("тип аргс", type(args))
    print(args)
    for i, arg in enumerate(args):
        print("пример:", i, arg)


print_Them_all(1, 44, "no")

#8.
def print_Them_all(*args):
    print("bla bla bla")
    print("тип аргс", type(args))
    print(args)
    for i in enumerate(args):
        print("пример:", i)

list = 123, "kusok", 18,96, 1111, "сами вы **", "лох!"
print_Them_all(1, 44, "no", list)
#print_Them_all(*list)

#9
def print_Them_all(**args):
    print("bla bla bla")
    print("тип аргс", type(args))
    print(args)
    for i in enumerate(args):
        print("пример:", i)


print_Them_all(name="Vasya", live="in Moscow")


#10.
def print_them_all(args):
    print("тип аргов:", type(args))
    print(args)
    for i in enumerate(args):
        print("аргумент номер:", i)


list = [1, 2, 666, "tuple"]
print_them_all(args=list)

#11.
def print_them_all(a, b=5, *args, **kwargs):
    print("тип аргов:", type(args))
    print(a, b)
    print(args)
    for i in enumerate(args):
        print("аргумент номер:", i)
    print("тип кваргов:", type(kwargs))
    for f in kwargs.items():
        print("аргумент кварга номер:", f)


print_them_all(1, 2, 3, "cat", name="Castiel", last_name="winchester", age=1000000000)
# print_them_all(1, 2, 666, "tuple")

#12. ТУТ НАДО НАЙТИ ОШИБКУ
from random import choice, randint

pw = randint(30, 35)
qua = randint(5, 45)


class adding:

    def __init__(self):
        self.s = []

    def randy(self, pw):

        self.s.append(pw)

    def spisok(self):
            for pw in self.s:
                print(pw)


s1 = adding()
while len(s1) < qua:
    adding.spisok(pw=randint(30, 35))