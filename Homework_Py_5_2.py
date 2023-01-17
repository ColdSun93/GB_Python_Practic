# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

import random


def game(name1, name2, sweets, max_sweet, param):
    first_turn = random.choice([name1, name2])
    flag = name1 if first_turn == name1 else name2

    while sweets > 0:
        print(f"Ход игрока {flag}")

        if flag == name1:
            turn = step_play(max_sweet)
            sweets -= turn
            if sweets > 0:
                print(f'конфет осталось - {sweets}')
            else:
                print(f'конфет осталось - 0')

            flag = name2 if flag == name1 else name1
        else:
            if param == 1:
                turn = random.randint(1, max_sweet)
            elif param == 2:
                turn = pve_smart(sweets,max_sweet)
            else:
                turn = step_play(max_sweet)
            print(f"{name2} взял {turn} конфет")
            sweets -= turn

            if sweets > 0:
                print(f'конфет осталось - {sweets}')
            else:
                print(f'конфет осталось - 0')

            if sweets < max_sweet:
                max_sweet = sweets

            flag = name2 if flag == name1 else name1

    winner = name2 if flag == name1 else name1
    print(f"Поздравляем победил игрок {winner}")

def step_play(step_max):
    step = int(input("введите желаемое количество конфет для взятия- "))
    while not 0 < step <= step_max:
        print("Введите конфеты в диапазоне от 0 до ", step_max)
        step = int(input("введите желаемое количество конфет для взятия- "))
    return step

def pve_smart(sweets,max_sweet):
    if sweets == max_sweet:
        return sweets
    elif sweets % max_sweet == 0:
        return max_sweet-1
    else:
        return sweets % max_sweet-1


sweets_play = int(input("Введите желаемое количество конфет - "))
max_step = int(input("Введите максимум конфет за ход "))
play_games = int(
    input("Выберите режим: 1-stupid bot, 2-smart bot, 3-two plaers "))
while not 0 < play_games <= 3:
    play_games = int(input("Введите количество игроков: 1,2 или 3 "))
name_play_one = input("Введите имя игрока - ")
if play_games == 1:
    name_play_two = "bot stupid"
elif play_games == 2:
    name_play_two = "bot smart"
else:
    name_play_two = input("Введите имя второго игрока - ")

game(name_play_one, name_play_two, sweets_play, max_step, play_games)
