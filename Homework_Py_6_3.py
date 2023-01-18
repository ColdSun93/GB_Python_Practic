# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def deg_num(num, deg):
    if deg==0:
        return 1
    elif deg==1:
        return num
    elif deg<0:
        return 1/(num*deg_num(num, -deg-1))
    else:
        return num*deg_num(num, deg-1)


numer = int(input("введите число "))
degre = int(input("введите степень (целое)  "))
result = deg_num(numer,degre)
print(result)
