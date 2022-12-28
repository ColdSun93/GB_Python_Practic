# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def Open_file(name):
    str_file = ''
    file = open(name, 'r')
    str_file = file.read()
    file.close
    return str_file

def Diction_elen(array_exp):
    diction_array_exp = {}
    for i in array_exp:
        if i.find('x') == -1 and i != '=' and i != '0' and i != '+':
            diction_array_exp.update([('0', i)])
        elif i.find('*x^') != -1:
            diction_array_exp.update(
                [(i.partition('*x^')[2], i.partition('*x^')[0])])
        elif i.find('*x') != -1:
            diction_array_exp.update([('1', i[0:-2])])
    return diction_array_exp

expres_one = Open_file('expression1.txt').split()
expres_two = Open_file('expression2.txt').split()
expres_one_sl = Diction_elen(expres_one)
expres_two_sl = Diction_elen(expres_two)
array_kf = []
size = 0

print(expres_one)
print(expres_one_sl)

print(expres_two)
print(expres_two_sl)

while len(expres_one_sl) != 0 or len(expres_two_sl) != 0:
    if expres_one_sl.get(str(size)) != None:
        array_kf.insert(0, int(expres_one_sl.pop(str(size))))
    elif expres_two_sl.get(str(size)) != None:
        array_kf.insert(0, int(expres_two_sl.pop(str(size))))
    else:
        array_kf.insert(0, 0)
    size +=1


size-=1
resul_str = ''
for i in range(size):
    if (array_kf[i] != 0) and (i < size-1):
        resul_str = resul_str + str(array_kf[i]) + '*x^' + str(size-i) + ' + '
    elif (array_kf[i] != 0) and (size-i == 1) and (array_kf[i+1] != 0):
        resul_str = resul_str + \
            str(array_kf[i]) + '*x' + ' + ' + str(array_kf[i+1]) + ' = 0'
    elif (array_kf[i] != 0) and (size-i == 1) and (array_kf[i+1] == 0):
        resul_str = resul_str + str(array_kf[i]) + '*x' + ' = 0'
    elif (size-i == 1) and (array_kf[i+1] != 0):
        resul_str = resul_str + str(array_kf[i+1]) + ' = 0'

print(resul_str)