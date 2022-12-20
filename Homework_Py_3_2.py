# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

spisok_one = [2, 3, 4, 5, 6]
spisok_result = []
for i in range(math.ceil(len(spisok_one)/2)):
    spisok_result.append(spisok_one[i]*spisok_one[(-1)-i])
print(spisok_result)