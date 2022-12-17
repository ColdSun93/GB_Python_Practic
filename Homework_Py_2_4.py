# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('введите число '))
array = [x for x in range(-number, number+1)]
print(f'Созданный массив: {array}')

path = 'file.txt'
ar_elem=[]
file = open(path, 'r')
for line in file:
    ar_elem.append(int(line.replace("\n", "")))
file.close

p=1
print(f'Произведение элементов ', end ="")
for i in ar_elem:
    p *=array[i]
    print(f'{array[i]}, ', end ="")
print(f'= {p}')
