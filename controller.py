import view
import model
inner_db = []

def programm_run ():
    choice = view.main_menu()
    match choice:
        case 1:
            headers = ['fist_name', 'last_name', 'phone', 'comment']
            inner_db = model.new_add_to_base(model.new_input_line(), headers)
        case 2:
            inner_db = model.file_import(model.op_file_name())
        case 3:
            model.file_export(model.op_file_name(), inner_db)
        case 4:
            model.printing_inner_db(inner_db)
        case _:
            print('Не известный параметр ввода.')
    view.main_menu()
    choice = view.main_menu()
