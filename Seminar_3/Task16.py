# Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

def input_numbers(input_text):
    while True:
        try:
            number = int(input(input_text))
            return number
        except ValueError:
            print('Ошибка! Введите число')

n = input_numbers('Введите количество элементов в массиве - ')
x = input_numbers(f'Введите число, которое надо проверить - ')
list_1 = []
for i in range(n):
    list_1.append(randint(1, n))
print(n)
print(list_1)
print(x)
print(f'Число {x} в массиве встречается {list_1.count(x)} раз')
