import view
import random
# user_list = [{'Фамилия':'Иванов'},{'Имя':'Иван'},{'Предмет':'Физика'}, {'Оценка':'5'}, {'Фамилия':'Смирнов'},{'Имя':'Семен'},{'Фамилия':'Иванов'},{'Предмет':'Физика'}, {'Оценка':'5'}]
user_list = {'Иванов Иван': {'Физика': [5, 4, 4], 'Физ-ра': [5, 4, 4], 'История': []},
             'Смирнов Семен': {'Физика': [5], 'Физ-ра': [5, 4], 'История': []}, 'Петров Петр': {'Физика': [5, 4, 4], 'Физ-ра': [5, 4, 4], 'История': [3]}}
valuation_list = ['Физика', 'Физ-ра', 'История']

name_list_rnd = ['Иван', 'Семен', 'Петр', 'Станислав', 'Александр', 'Сергей', 'Владимир',
                 'Роман', 'Кирилл', 'Данил', 'Егор', 'Адмам', 'Андрей', 'Игорь', 'Павел', 'Максим']
surname_list_rnd = ['Иванов', 'Смирнов', 'Петров', 'Сидоров', 'Галкин', 'Смолин',
                    'Кузнецов', 'Виноградов', 'Никонов', 'Агапов', 'Гуров', 'Фролов', 'Фомин', 'Юдин']


def init(array=[]):
    global user_list
    global valuation_list
    global name_list_rnd
    global surname_list_rnd
    array = user_list
    return array


def add_random_stud():
    name_list = random.sample(name_list_rnd, 10)
    surname_list = random.sample(surname_list_rnd, 10)
    fio_list = []
    # surname_list = list(range(1, 11))
    # print(name_list[0])
    for i in surname_list:
        for j in name_list:
            fio_list.append(i+' '+j)
    
    for fio in fio_list:
        dic_val_les={}
        for dic in valuation_list:
            dic_val_les[dic]=[random.randint(1,5)]
        user_list[fio]= dic_val_les
    return user_list
    # user_list


# a = add_random_stud(name_list_rnd, surname_list_rnd)
# print(a)


def add_student():
    name_stud = input('Введите Имя и Фамилию студента ')
    dic_val_les={}
    for dic in valuation_list:
        dic_val_les[dic]=[]
    user_list[name_stud] = dic_val_les
    print('1 - продолжить ввод;  2 - завершить ввод')
    key = choice_option()
    if key == 1:
        return add_student()
    else:
        return user_list


def add_valuation():
    name_stud = str(input('Введите фамилию и имя студента '))
    if name_stud in user_list:
        name_lesson = str(input('Введите Предмет '))
        if name_lesson in valuation_list:
            val_stud = int(input('Введите оценку '))
            for keys, val in user_list.items():
                for key_two, value_two in val.items():
                    if keys == name_stud and key_two == name_lesson:
                        value_two.append(val_stud)
        else:
            print('Предмет не найден, 1-повторить ввод 2-завершить')
            key = choice_option()
            if key == 1:
                return add_valuation()
            else:
                return user_list
    else:
        print('Студент не найден, 1-повторить ввод 2-завершить')
        key = choice_option()
        if key == 1:
            return add_valuation()
        else:
            return user_list
    return user_list


def add_lesson():
    object = str(input('Введите предмет '))
    if object in valuation_list:
        print('Предмет уже есть в базе, 1-повторить ввод 2-завершить ввод')
        key = choice_option()
        if key == 1:
            return add_lesson()
    add_lesson_student(object)
    return user_list


def add_lesson_student(lesson, valuation=[]):

    for value in user_list.values():
        value[lesson] = valuation
    return user_list


def choice_option():
    num = int(input())
    if num == 1 or num == 2:
        return num
    else:
        print('Неверный ввод, введите заново')
        return choice_option()
