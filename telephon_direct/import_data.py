import controller as cont

data = []


def init(array=[]):
    global data
    data = array


def Open_file(name):
    file = open(name, 'r')
    for line in file:
        data.append(str(line[:-2].replace("\n", "")).split('\t',4))
    file.close
    return data


def write_data():
    id = input('Введите id ')
    name = (input('Введите имя '))
    surname = (input('Введите фамилию '))
    telephone = (input('Введите телефон '))
    comment = (input('Введите комментарий '))
    
    str_data = id+' | '+ name+' | '+surname+' | '+telephone+' | '+comment
    # str_data = [1, 23, 34, 45, 56]
    data.append(list(map(str, str_data.split(' | '))))
    # data.append(list(map(int, str_data)))
    print('1 - продолжить ввод;  0 - завершить ввод')
    key = cont.get_module()
    if key == 1:
        return write_data()
    elif key == 0:
        return data
