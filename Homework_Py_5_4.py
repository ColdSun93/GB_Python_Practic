# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв



def Coding_rle(str_data):
    # str_data = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
    if not str_data: return ''
    previous_char = ''
    str_result = ''
    count = 1

    for char in str_data:
        if char != previous_char:
            if previous_char != '':
                str_result += str(count) + previous_char
            count = 1
            previous_char = char
        else:
            count += 1
    str_result += str(count) + previous_char
    return str_result

def Decoding_rle(str1_data):
    if not str1_data: return ''
    decode = '' 
    count = '' 
    for char in str1_data: 
        if char.isdigit(): 
            count += char 
        else:
            decode += char * int(count) 
            count = '' 
    return decode



data = str(input('Введите строку: '))
key = int(input('Введите операцию 1- кодирование, 2 - декодирование: '))

if key==1: 
    result = Coding_rle(data)
    print(result)
elif key==2:
    result = Decoding_rle(data)
    print(result)
else:
    print('error')
