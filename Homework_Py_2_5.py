# Реализуйте алгоритм перемешивания списка.

import random
size = int(input('введите количество элементов '))
array = []
for i in range(size):
    array.append(random.randint(-10, 10))
print(array)

# random.shuffle(array)

# Перемешивает левую половину с правой в рандомном порядке
size_range=int(size/2)
array2=random.sample(range(size_range, size), size_range)
for i in range(size_range):
    temp = array[i]
    array[i] = array[array2[i]]
    array[array2[i]] = temp

print(array)