import csv

def read_file(file):
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        temp = []
        for row in reader:
            temp.append(row)
        return temp

def print_contacts(list_contact: list):
    if len(list_contact) == 0:
        print('Справочник пустой. Добавьте контакт.')
    else:
        for i in range(len(list_contact)):
            print(list_contact[i]['last_name'], list_contact[i]['first_name'],
                  list_contact[i]['surname'], list_contact[i]['phone_number'])
