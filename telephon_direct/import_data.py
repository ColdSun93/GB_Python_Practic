import controller as cont

data = []

def init(array=[]):
    global data
    data = array

def Open_file(name):
    file = open(name, 'r')
    for line in file:
        data.append(line("\n", "").split)
    file.close
    return data

def write_data():
    id = (input('Введите id '))
    name = (input('Введите имя '))
    surname = (input('Введите фамилию '))
    telephone = (input('Введите телефон '))
    comment = (input('Введите комментарий '))
    data.append(id+name+surname+telephone+comment)
    print('1 - продолжить ввод;  0 - завершить ввод')
    key = cont.get_module()
    if key == 1:
        return write_data(data)
    elif key == 0:
        return data

