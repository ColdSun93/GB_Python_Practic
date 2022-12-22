# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = 8
# int(input('введите целое число '))
n_fibonachi = [-1, 1, 0, 1]
for i in range(4, n+3):
    n_fibonachi.append(n_fibonachi[i-1]+n_fibonachi[i-2])

for j in range(n-2):
    n_fibonachi.insert(0,n_fibonachi[1]-n_fibonachi[0])
print(n_fibonachi)