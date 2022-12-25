# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('введите число '))
array = []
count = 2
while n != 1:
    if n % count == 0:
        array.append(count)
        n /= count
        count = 2
    else:
        count += 1
print(array)
