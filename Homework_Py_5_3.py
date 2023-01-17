# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, 
# каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, 
# и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

import random

maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def check_victories():
    for i in victories:
        if maps[i[0]] == maps[i[1]] == maps[i[2]]:
            return True
    return False

def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

print_maps()

name1 = input("Введите имя первого игрока - ")
name2 = input("Введите имя второго игрока - ")
first_turn = random.choice([name1,name2])

print(first_turn)
game_over = False

cur_turn = first_turn

while not game_over:
    if cur_turn == first_turn:
        symbol = "X"
        step = int(input("введи клетку от 1 до 9, куда хочешь ходить "))
        if maps[int(step) - 1] == "X" or maps[int(step) - 1] == "0":
            print("Неверный ввод")
            continue
        maps[step-1] = symbol
    else:
        symbol = "0"
        step = int(input("введи клетку от 1 до 9, куда хочешь ходить "))
        if maps[int(step) - 1] == "X" or maps[int(step) - 1] == "0":
            print("Неверный ввод")
            continue
        maps[step - 1] = symbol
    print_maps()
    if check_victories():
        print(f"победил игрок {cur_turn}")
        game_over = True
    cur_turn = name2 if cur_turn == name1 else name1