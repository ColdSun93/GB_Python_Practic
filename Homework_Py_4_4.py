# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

size = int(input('Введите натуральную степень '))
array_kf = [random.randint(0, 100) for i in range(size+1)]
print(array_kf)

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

my_file = open("result.txt", "w")
my_file.write(resul_str)
my_file.close()