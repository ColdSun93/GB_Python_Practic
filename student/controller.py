import view
import storage_data as sd

def button_click():
    print('Введите операцию: 1 - отобразить список, 2 - добавить предмет, 3 - добавить студента, 4 - добавить оценки студенту, 5 - вывести информацию на экран, 6 - завершить работу')
    oper = view.get_module()
    direct = sd.init()
    if oper==1:
        direct = view.show_user(direct)
    elif oper==2:
        direct = sd.add_lesson()
    elif oper==3:
        direct = sd.add_student()
    elif oper==4:
        direct = sd.add_valuation()
        print(direct)
    elif oper==5:
        view.show_user(direct)
    elif oper==6:
        quit()
    view.show_all_user(direct)
    quit()


