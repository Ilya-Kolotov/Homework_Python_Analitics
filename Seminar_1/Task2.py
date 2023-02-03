# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def sum_digit(number):
    sum_digit = 0
    while number > 0:
        sum_digit += number % 10
        number //= 10
    return sum_digit

num = int(input('Введите число - '))
sum_digits = sum_digit(num)
print(f'Сумма цифр числа {num} = {sum}')