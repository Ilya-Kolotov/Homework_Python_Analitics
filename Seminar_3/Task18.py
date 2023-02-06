# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5
from  random import randint

def input_numbers(input_text):
    while True:
        try:
            number = int(input(input_text))
            return number
        except ValueError:
            print('Ошибка! Введите число')


def check_elem(list_check):
    diff = []
    for j in range(len(list_check)):
            diff.append(abs(x - list_check[j]))
    check_num = 0
    for i in range(len(diff)):
        if diff[i] == min(diff):
            check_num = list_check[i]
    return check_num

n = input_numbers('Введите количество элементов в массиве - ')
x = input_numbers(f'Введите число, которое надо проверить - ')
list_1 = [randint(1, n) for i in range(n)]
check_num = check_elem(list_1)

print(n)
print(*list_1)
print(x)
print(f'Ближайший элемент по величине близкий к {x} = {check_num}')