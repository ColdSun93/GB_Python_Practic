import storage_data as sd

def get_module():
    num = int(input())
    if 0 < num < 8:
        return num
    else:
        print('Неверный ввод, введите заново')
        return get_module()

def show_user(direct):
    print('Выберете вывод: 1 - вывести список студентов, 2- вывести оценки студента')
    key = sd.choice_option()
    if key == 1:
        print('Cписок студентов:')
        for key_fio in direct.keys():
            print(f'{key_fio} ')
        return 
    else:
        show_valuation_user(direct)

        return 

def show_valuation_user(direct):
    name_stud = input('Введите Фамилию и Имя студента ')
    for key, value in direct.items():
        if key == name_stud:
            print(f'Оценки студента {key}:')
            for key_two,value_two in value.items():
                print(f'Предмет: {key_two} Оценка:{value_two}')
    return

def show_all_user(direct):
    print('Cписок студентов и оценок:')
    for key, value in direct.items():
        print(f'Студент: {key}')
        for key_two,value_two in value.items():
            if len(value_two)==0:
                avg_val=0
            else:
                avg_val=round(sum(value_two)/len(value_two),2)
            print(f'Предмет: {key_two} Оценки:{value_two} Средний бал:{avg_val}')
    return