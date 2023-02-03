# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(input_text))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number


def sum_digit(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def check_lucky_ticket(number):
    num1 = number % 1000
    num2 = number // 1000
    sum1 = sum_digit(num1)
    sum2 = sum_digit(num2)
    if sum1 == sum2:
        return f'счастливый'
    else:
        return f'не счастливый'

ticket = input_numbers('Введите номер билета: ')
if len(str(ticket)) == 6:
    lucky = check_lucky_ticket(ticket)
    print(f'Билет {ticket} - {lucky}')
else:
    print('Введен неправильный номер билета')