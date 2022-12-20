# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spisok_one = [1.1, 1.2, 3.1, 5, 10.01]
spisok_temp = []
for i in range(len(spisok_one)):
    if spisok_one[i] % 1 != 0:
        spisok_temp.append(spisok_one[i] % 1)
result = round(max(spisok_temp)-min(spisok_temp), 2)
print(result)
