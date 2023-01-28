import view
import storage_data as sd
import work_file as wf

name_file = 'student/direct_student.txt'

def button_click():
    print('Введите операцию: 1 - Сгенерировать рандомно, 2 - добавить предмет, 3 - добавить студента, 4 - добавить оценки студенту, 5 - вывести информацию на экран, 6 - загрузить из файла, 7 - завершить работу')
    oper = view.get_module()
    direct = sd.init()
    if oper==1:
        direct = sd.add_random_stud()
        print(direct)
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
        direct = wf.Open_file(name_file)
    elif oper==7:    
        quit()

    view.show_all_user(direct)
    print('Выберете операцию: 1 - записать в файл или 2 - продолжить и выйти ')
    operator_save = sd.choice_option()
    oper_file = "w"
    if operator_save == 1:
        oper_file = "w"
        wf.Save_file(name_file, direct, oper_file)
    
    quit()


