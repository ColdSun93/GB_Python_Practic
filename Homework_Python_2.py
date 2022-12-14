# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):

            left_expres = x == 1 or y == 1 or z == 1
            right_expres = x == 0 and y == 0 and z == 0
            print(left_expres)
