# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def input_numbers(input_text):
    while True:
        try:
            number = int(input(input_text))
            return number
        except ValueError:
            print('Ошибка! Введите число')


first_elem = input_numbers("Введите первый элемент - ")
d = input_numbers("Введите разность - ")
num = input_numbers("Введите количество элементов - ")
an = [first_elem + (i -1)*d for i in range(1, num+1)]
print(f"Первый элемент = {first_elem}, разность = {d}, количество элементов = {num}")
print(f"Арифметическая прогрессия = {' '.join(map(str, an))}")
