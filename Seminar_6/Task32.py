# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def input_numbers(input_text):
    while True:
        try:
            number = int(input(input_text))
            return number
        except ValueError:
            print('Ошибка! Введите число')

print("Задайте диапозон")
num_min = input_numbers("Введите минимум - ")
num_max = input_numbers("Введите максимум - ")
a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(f"Заданный массив {a}")
b = list(map(lambda x: x[0], filter(lambda x: x[1] <= num_max and x[1] >=num_min, enumerate(a))))
print(f"Индексы элементов массива, значения которых принадлежат заданному диапазону = {b}")