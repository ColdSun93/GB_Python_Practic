import view
# user_list = [{'Фамилия':'Иванов'},{'Имя':'Иван'},{'Предмет':'Физика'}, {'Оценка':'5'}, {'Фамилия':'Смирнов'},{'Имя':'Семен'},{'Фамилия':'Иванов'},{'Предмет':'Физика'}, {'Оценка':'5'}]
user_list = {'Иванов Иван': {'Физика': [5, 4, 4], 'Физ-ра': [5, 4, 4], 'История': []},
             'Смирнов Семен': {'Физика': [5], 'Физ-ра': [5, 4], 'История': []}, 'Петров Петр': {'Физика': [5, 4, 4], 'Физ-ра': [5, 4, 4], 'История': [3]}}
valuation_list = {'Физика': [], 'Физ-ра': [], 'История': []}


def init(array=[]):
    global user_list
    global valuation_list
    array = user_list
    return array


def add_student():
    name_stud = input('Введите Имя и Фамилию студента ')
    user_list[name_stud] = valuation_list
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
                    if keys==name_stud and key_two==name_lesson:
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
    valuation_list[object] = []
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

