import csv
import os
import view

file = 'export_data.csv'
def init_user(last_name, first_name, surname, phone_number):
    return last_name, first_name,surname,phone_number


def init_file(name: str):
    file = name+'.csv'
    return file
def save_data_to_file(data: tuple, file, mode='a'):
    fieldnames = ['last_name', 'first_name', 'surname', 'phone_number']
    dict_data = dict(zip(fieldnames, data))
    with open(file, mode, newline='', encoding='utf-8') as fd:
        writer = csv.DictWriter(fd, fieldnames=fieldnames)
        if os.path.getsize(file) == 0:
            writer.writeheader()
            writer.writerow(dict_data)
        else:
            writer.writerow(dict_data)


def choise_record(list_contact: list):
    for i in range(len(list_contact)):
        print(i + 1, list_contact[i]['last_name'], list_contact[i]['first_name'], list_contact[i]['surname'],
              list_contact[i]['phone_number'])
    choise_record = view.get_value_number('Выберите порядковый номер записи - ')
    return choise_record


def delete_record(list_contact: list, choise_record):
        list_contact.pop(choise_record - 1)
        fieldnames = ['last_name', 'first_name', 'surname', 'phone_number']
        with open(file, 'w', newline='', encoding='utf-8') as fd:
            writer = csv.DictWriter(fd, fieldnames=fieldnames)
            writer.writeheader()
            for i in list_contact:
                writer.writerow(i)
def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'last_name', '2': 'first_name', '3': 'phone_number'}
    found_contacts = []
    for contact in list_contacts:
        if param == '4':
            if contact['last_name'] == what.split()[0] and contact['first_name'] == what.split()[1]:
                found_contacts.append(contact)
        elif contact[param_dict[param]] == what:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден')
    else:
        return found_contacts


def change_contact(list_contact: list, choise_record, param: str, what: str, mode, new_file: str):
    param_dict = {'1': 'last_name', '2': 'first_name', '3': 'surname', '4': 'phone_number'}
    change_contact = []
    change_contact.append(list_contact.pop(choise_record - 1))
    change_contact[0][param_dict[param]] = what
    list_contact.insert(choise_record - 1, change_contact[0])
    fieldnames = ['last_name', 'first_name', 'surname', 'phone_number']
    if mode == 1:
        with open(file, 'w', newline='', encoding='utf-8') as fd:
            writer = csv.DictWriter(fd, fieldnames=fieldnames)
            writer.writeheader()
            for i in list_contact:
                writer.writerow(i)
    else:
        with open(new_file, 'a', newline='', encoding='utf-8') as fd:
            writer = csv.DictWriter(fd, fieldnames=fieldnames)
            writer.writeheader()
            for i in list_contact:
                writer.writerow(i)
