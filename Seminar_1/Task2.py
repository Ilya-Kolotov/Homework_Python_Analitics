# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def sum_digit(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

num = int(input('Введите число - '))
sum = sum_digit(num)
print(f'Сумма цифр числа {num} = {sum}')