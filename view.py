def main_menu ():
    print('\n'
        'Для работы со справочником, выберите опцию: \n'
        "1 - Добавить новую запись в справочник.\n"
        "2 - Импортировать справочник из файла.\n"
        "3 - Экспортировать справочник в файл.\n"
        "4 - Показать текущие данные справочника.\n"
        "5 - Прервать работу с программой (не забудьте сохранить данные).")
    number = int(input())
    if 0 < number < 5:
        print(f"Ваш выбор: {number}")
    elif number == 5: 
        print ('Хорошего дня!')
        quit()
    else: print("Не существующая опция")
    return number



