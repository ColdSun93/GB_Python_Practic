import import_data as wd
import export_data as ed

name_file = '\Telephon_direct\Telephon_direct\Telephon_direct.txt'


def button_click():
    print('Выберете операцию: 1 - ввод новых данных или 0 - импорт из файла')
    operator_add = get_module()
    direct = wd.do_it_sum()
    if operator_add == 1:
        direct = wd.write_data(direct)
    elif operator_add == 0:
        direct = wd.Open_file(name_file)
    view_data(direct)
    print('Выберете операцию: 1 - перезаписать файл или 0 - дополнить файл')
    operator_save = get_module()
    if operator_save == 1:
        ed.Save_file(direct)
    elif operator_save == 0:
        ed.Overwrite_file(direct)


def get_module():
    num = int(input())
    if num == 0 or num == 1:
        return num
    else:
        print('Неверный ввод, введите заново')
        return get_module()


def view_data(direct):
    for i in direct:
        print(f'{i}')
