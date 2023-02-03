# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2
from random import randint
def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(input_text))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number


def min_flip_coins(number):
    count_tails = 0
    count_coat = 0
    for i in range(number):
        side_coin = randint(0 ,1)
        print(side_coin, end= ' ')
        if side_coin == 0:
            count_tails += 1
        else:
            count_coat += 1
    if count_coat < count_tails:
        return count_coat
    else:
        return count_tails

num_coins = input_numbers('Введите количество монет - ')
count_flip_coins = min_flip_coins(num_coins)
print(f'\nЧтобы все монеты лежали одинаковыми надо перевернуть {count_flip_coins} шт.')
