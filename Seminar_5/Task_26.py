# Задача 26
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3**5)
# A = 2; B = 3 -> 8

def digit_in_pow(a, b):
    if b == 1:
        return a
    return digit_in_pow(a, b - 1) * a

a = int(input('Введите первое число - '))
b = int(input('Введите второе число - '))
digit_in_pow = digit_in_pow(a, b)
print(digit_in_pow)
