from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_size = 20

_holder = {}  # где будет храниться наша позиция, это какая-то внутренняя переменная, которую использовать напрямую не надо, это сигнал другим программиста


def put_stones():
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES+1):
        _holder[i]=(randint(1, MAX_BUNCHES_size))  # append - это добавление в конце


def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_bunches(): #позиция камней
    res = []
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res


def is_game_over():
    return sum(_holder.values()) == 0
