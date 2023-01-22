import import_data as wd
import export_data as ed
import sorp_direct as sd

name_file = 'Telephon_direct/Telephon_direct.txt'


def button_click():
    print('Выберете операцию: 1 - ввод новых данных или 0 - импорт из файла')
    operator_add = get_module()
    direct = wd.init()
    if operator_add == 1:
        direct = wd.write_data()
    elif operator_add == 0:
        direct = wd.Open_file(name_file)
        print('Выберете операцию: 1 - добавить данные или 0 - отсортировать')
    operator_imp = get_module()
    if operator_imp == 1:
        direct = wd.write_data()
    elif operator_imp == 0:
        direct = sd.sort_table(direct)

    view_data(direct)
    print('Выберете операцию: 1 - перезаписать файл или 0 - дополнить файл')
    operator_save = get_module()
    oper_file = "w"
    if operator_save == 1:
        oper_file = "w"
    elif operator_save == 0:
        oper_file = "a"
    ed.Save_file(name_file, direct, oper_file)
    print('finish')


def get_module():
    num = int(input())
    if num == 0 or num == 1:
        return num
    else:
        print('Неверный ввод, введите заново')
        return get_module()


def view_data(direct):
    print('Выберете операцию: 1 - вывести все данные или 0 - вывести только имя и фамилию')
    key_view = get_module()
    if key_view ==1:
        for i in direct:
            print(f'{i}')
    elif key_view ==0:
        for i in direct:
            print(f'{i[1],i[2]}')
