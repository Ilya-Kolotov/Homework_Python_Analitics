# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3
from math import sqrt

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(input_text))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number


def guess_numbers(a, b):
    d = (-a) ** 2 - 4 * b
    if d < 0:
        print('Отгадать числа невозможно')
    elif d == 0:
        x = y = a / 2
        return x, y
    else:
        y = (a + sqrt(d)) / 2
        x = (a - sqrt(d)) / 2
        return x, y
print('Загадайте 2 числа в диапозоне от 0 до 1000')
sum_num = input_numbers('Введите сумму этих чисел - ')
mult_num = input_numbers('Введите произведение этих чисел - ')
if 0 <= sum_num <= 2000 and mult_num >= 0:
    x = int(guess_numbers(sum_num, mult_num)[0])
    y = int(guess_numbers(sum_num, mult_num)[1])
    print(f'Загаданные числа - {x}, {y}')
else:
    print('Загаданные числа не входят в диапозон')