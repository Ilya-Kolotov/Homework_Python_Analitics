# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint

def create_list(x):
    new_list = [randint(1, 10) for i in range(x)]
    return new_list


def create_set(list):
    new_set = set(list)
    return new_set

n = int(input('Введите количество чисел в первом множестве - '))
m = int(input('Введите количество чисел во втором множестве - '))
list_1 = create_list(n)
list_2 = create_list(m)
set_1 = create_set(list_1)
set_2 = create_set(list_2)
res_set = set_1 & set_2
res_list = list(res_set)
res_list.sort()
print(*res_list)
