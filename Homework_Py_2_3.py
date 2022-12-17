# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

number = int(input('введите число '))
array = []
sum = 0
for i in range(1, number+1):
    array.append((1+1/i)**i)
    print(f"{i}: {round(array[i-1],2)}, ",end ="")
    sum += array[i-1]
print()
print(f'Сумма элементов равна {round(sum,2)}')