
# def action_choice (num: int ) -> def:


inner_db = []
headers = ['fist_name', 'last_name', 'phone', 'comment']

def new_input_line () -> list:
    fst_name = input("Введите Имя: ")
    lst_name = input("Введите фамилию: ")
    phone_num = str(input("Введите номер телефона в любом формате: "))
    cmmnt = input("Введите описание/комментарий: ")
    new_user = [fst_name, lst_name, phone_num, cmmnt]
    return new_user

def new_add_to_base (headers, new_user):
    inner_db_line = dict(zip(headers, new_user))
    inner_db.append(inner_db_line)
    print(f"Запись {inner_db_line.keys()} добавлена")
    return inner_db

def op_file_name ():
    file_name = str(input('Введите имя файла (без расширения, добавится автоматически): '))
    file_name += '.csv'
    return file_name

#export to file, converting to nested dictionary 1st
def file_export (file_name: str, inner_db: list):
    imp_inner_db = {i : inner_db[i] for i in range (0, len(inner_db))}
    db_end = 'end of data base' 
    record_end = '***'
    separator = ' : '
    export_file = open(file_name, 'a')
    for key in imp_inner_db:
        print(key, file = file_name)
        for (name, value) in imp_inner_db[key].items():
            print(name + separator + repr(value), file = export_file)
            print(record_end, file = export_file)
    print(db_end, file = export_file)
    export_file.close()
    print (f'Файл {file_name} был создан или обновлен.')

# import from file, and storing in list of dicts
def file_import (file_name: str):
    db_end = 'end of data base' 
    record_end = '***'
    separator = ' : '
    import_file = open(file_name)
    import sys
    sys.stdin = import_file
    inner_db_dict = {}
    key = input()
    while key != db_end:
        inner_db_line = {}
        data = input()
        while data != record_end:
            name, value = data.split(separator)
            inner_db_line[name] = eval(value)
            data = input()
        inner_db_dict[key] = inner_db_line
        key = input()
    print (f'Данные из файла {file_name} были выгружены в программу.')
    return list[inner_db_dict.values]


def printing_inner_db (inner_db: list):
    i = 0
    print('Текущая база данных содержит следующие записи:')
    while i < len(inner_db):
        print(inner_db[i].values())
        i += 1









