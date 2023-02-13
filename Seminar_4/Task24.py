# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
from random import randint

def create_list(x):
    new_list = [randint(1, 10) for i in range(x)]
    return new_list


def find_max_harvest(list_in):
    max_harvest = list_in[-1] + list_in[0] + list_in[1]
    for i in range(1, len(list_in) - 1):
        harvest = list_in[i - 1] + list_in[i] + list_in[i + 1]
        if  harvest > max_harvest:
            max_harvest = harvest
    harvest = list_in[-1] + list_in[0] + list_in[-2]
    if harvest > max_harvest:
        max_harvest = harvest
    return max_harvest

n = int(input('Введите количество кустов на грядке - '))
garden_list = create_list(n)
print(garden_list)
max_harvest = find_max_harvest(garden_list)
print(max_harvest)
