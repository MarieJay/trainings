#1.
import nim_engine
# print(probe.variable)
# probe.function1()
print(dir(nim_engine))

from nim_engine import variable as v1
print(v1)

from nim_engine import *
function1()
print(variable)

#2.
import math
print(math.sin(math.pi/2))
print(math.sin(1.6))

import sys
for path in sys.path:
    print(path)

#3.

def path():
    from sys import path
    return path
print(path())

#4.
from package_1 import module_1

module_1.function_1()

#5. nim_engine
from nim_engine import put_stones, take_from_bunch, is_game_over, get_bunches
from termcolor import colored, cprint

put_stones()
user_number = 1
while True:
    cprint("начальная позиция:", "white")
    cprint(get_bunches(), "white")
    user_color = "cyan" if user_number == 1 else "magenta"
    cprint("Ход игрока {}".format(user_number), color=user_color)
    posit = input(colored("Откуда берем?", color=user_color))
    quant = input(colored("Сколько берем?", color=user_color))
    success = take_from_bunch(int(posit), int(quant))
    if success:
        user_number: int = 2 if user_number == 1 else 1
    else:
        cprint("Ход невозможен", "red")
    if is_game_over():
        break


cprint("выйграл игрок номер {}".format(user_number), color="red")

#6.

from random import choice, randint

print("1:", randint(2, 8))
print("2:")
word = choice([11, 20, 10])
print(word)
help(choice)