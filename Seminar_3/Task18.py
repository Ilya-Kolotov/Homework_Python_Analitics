# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

# ver 1 по условию задачи

# def input_numbers(input_text):
#     while True:
#         try:
#             number = int(input(input_text))
#             return number
#         except ValueError:
#             print('Ошибка! Введите число')
#
#
# def check_elem(list_check):
#     if x >= list_check[-1]:
#         check_num = list_check[-1]
#         return check_num
#     elif x <= list_check[0]:
#         check_num = list_check[0]
#         return check_num
#     else:
#         for i in range(1,len(list_check) - 1):
#             if x == list_check[i]:
#                 check_num = list_check[i]
#                 return check_num
#
# n = input_numbers('Введите количество элементов в массиве - ')
# x = input_numbers(f'Введите число, которое надо проверить - ')
# list_1 = [i for i in range(1, n + 1)]
# check_num = check_elem(list_1)
# print(n)
# print(*list_1)
# print(x)
# print(f'Ближайший элемент по величине близкий к {x} = {check_num}')

# ver 2 with random

from random import randint

def input_numbers(input_text):
    while True:
        try:
            number = int(input(input_text))
            return number
        except ValueError:
            print('Ошибка! Введите число')


def check_elem(list_check, x):
    diff = []
    check_num = []
    for j in range(len(list_check)):
        if x > max(list_check):
            check_num.append(max(list_check))
            return check_num
        elif list_check[j] == x:
            check_num.append(list_check[j])
            return check_num
        else:
            diff.append(abs(x - list_check[j]))
    for i in range(len(diff)):
        if diff[i] == min(diff) and list_check[i] not in check_num:
            check_num.append(list_check[i])
            if len(check_num) > 2:
                return check_num
    return check_num

n = input_numbers('Введите количество элементов в массиве - ')
x = input_numbers(f'Введите число, которое надо проверить - ')
list_1 = [randint(1, n) for i in range(n)]
check_num = sorted(check_elem(list_1, x))
print(n)
print(*list_1)
print(x)
print(f'Ближайший(-е) элемент(-ы) по величине близкий(-е) к {x} =', ','.join(map(str, check_num)))