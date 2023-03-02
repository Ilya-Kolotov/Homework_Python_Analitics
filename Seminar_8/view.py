import validator


def get_value(text):
    result = input(text)
    while len(result) == 0:
        print('Поле не должно быть пустым. Введите значение: ')
        result = input()
    return result

def get_value_number(text):
    result = input(text)
    while not validator.is_num(result):
        print('Нужно ввести число. Попробуйте снова: ')
        result = input()
    return int(result)

def get_mode():
    modes = ['1', '2', '3', '4', '5', '6']
    mode = input('\n1 - Добавить новый контакт\n2 - Посмотреть справочник'
                 '\n3 - Удалить запись\n4 - Поиск по параметрам\n'
                 '5 - Изменить данные\n6 - Завершить программу\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)


def ask_search():
    print('По какому полю выполнить поиск?')
    search_params = ['1', '2', '3','4']
    search_param = input('1 - По фамилии\n2 - По имени\n3 - по номеру телефона\n4 - По фамилии и имени\nВыбери: ')
    while search_param not in search_params:
        print('Такого режима нет. Введите корректный: ')
        search_param = input()
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    elif search_param == '4':
        what = input('Введите фимилию и имя ')
    return search_param, what


def get_mode_change_contact():
    modes = ['1', '2', '3', '4']
    mode = input('\n1 - Изменить фамилию\n2 - Изменить имя'
                 '\n3 - Изменить отчество\n4 - Изменить номер телефона\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)


def ask_change_contact():
    print('Какое поля хотите изменить?')
    search_params = ['1', '2', '3','4']
    search_param = input('1 - Фамилию\n2 - Имя\n3 - отчество\n4 - Номер телефона\nВыбери: ')
    while search_param not in search_params:
        print('Такого режима нет. Введите корректный: ')
        search_param = input()
    what = input('Введите новые данные: ')
    return search_param, what


def ask_where_save_file():
    print('Куда сохранить файл?')
    modes = ['1', '2']
    mode = input('1 - Перезаписать существующий\n2 - Сохранить в отдельном файле\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return int(mode)