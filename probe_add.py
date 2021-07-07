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