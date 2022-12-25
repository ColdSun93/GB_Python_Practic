# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
size = int(input('введите количество элементов '))
array_one = [1, 2, 3, 4, 2, 5, 1, 2, 6, 3]
array_two = []
for i in range(size):
    array_one.append(random.randint(1, size+10))

for i in array_one:
    if array_one.count(i) < 2 or array_two.count(i) == 0:
        array_two.append(i)

print(array_one)
print(array_two)
