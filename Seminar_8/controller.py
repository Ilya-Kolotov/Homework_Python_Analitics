import view
import export_data
import import_data


def button():
    mode = view.get_mode()
    if mode == 1:
        last_name = view.get_value('Введите Фамилию: ')
        first_name = view.get_value('Введите Имя: ')
        surname = view.get_value('Введите Отчество: ')
        phone_number = view.get_value('Введите номер телефона: ')
        export_data.save_data_to_file(export_data.init_user(last_name, first_name, surname, phone_number),export_data.file)
        button()
    elif mode == 2:
        list_contact = import_data.read_file(export_data.file)
        import_data.print_contacts(list_contact)
        button()
    elif mode == 3:
        list_contact = import_data.read_file(export_data.file)
        choise_record = export_data.choise_record(list_contact)
        export_data.delete_record(list_contact, choise_record)
        button()
    elif mode == 4:
        search_param, what = view.ask_search()
        list_contact = import_data.read_file(export_data.file)
        res = export_data.search_contact(list_contact, search_param, what)
        if len(res) == 0:
            button()
        else:
            import_data.print_contacts(res)
            button()
    elif mode == 5:
        list_contact = import_data.read_file(export_data.file)
        choise_record = export_data.choise_record(list_contact)
        search_param, what = view.ask_change_contact()
        mode_file = view.ask_where_save_file()
        name = input('Введите название файла')
        new_file = export_data.init_file(name)
        export_data.change_contact(list_contact, choise_record, search_param, what, mode_file, new_file)
        button()
    else:
        return print('Программа завершена')