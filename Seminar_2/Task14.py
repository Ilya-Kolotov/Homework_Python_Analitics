# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(input_text))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number


def degrees_number(number):
    degree = 0
    digit_in_degree = 2 ** degree
    result = []
    while digit_in_degree <= number:
        result.append(digit_in_degree)
        degree += 1
        digit_in_degree = 2 ** degree
    return result

num = input_numbers('Введите число - ')
deg_number = degrees_number(num)
print(f'Целые степени двойки в диапозоне от 0 до {num} -',*deg_number)