import view
import log_data
import sys
import fileinput


# Режим создание файла/выбор доступных файлов


def get_op(mode_view):
    if mode_view == 1:
        name_fail = input('Наименование файла: ') + '.txt'
        with open(name_fail, 'w') as file:
            file.write('Database v.0.01')
            file.write('\nФамилия - Имя - Отчество - Номер телефона\n')
            print('\n=======================================')
            print(f'       Файл "{name_fail}" создан')
            print('=======================================\n')
        view.get_mode_change()
    elif mode_view == 2:
        if len(log_data.list_data_base) >= 1:
            print('\nСписок доступных файлов:')
            print('\n'.join(map(str, log_data.list_data_base)))
            print()
            view.get_mode_change()
        else:
            print('\n=======================================')
            print('Нет доступных файлов для редактирования')
            print('=======================================\n')
            view.get_two_start()

# Чтение текста из выбранного файла


def get_read(mode_change):
    name_file = input('\nВыберите справочник: ') + '.txt'
    if mode_change == 1:
        with open(name_file, 'r') as file:
            for text in file:
                print(text)
            file.readlines()
            file.close()
            view.get_mode_change()

# Добавление данных в файл


def get_input(mode_change):
    name_file = input('\nВыберите справочник: ') + '.txt'
    if mode_change == 2:
        text_surname = input('\nФамилия: ')
        text_name = input('Имя: ')
        text_patronymic = input('Отчество: ')
        text_number_phone = input('Номер телефона: ')
        with open(name_file, 'a') as file:
            file.write(
                f'{text_surname} - {text_name} - {text_patronymic} - {text_number_phone}\n')
        view.get_mode_change()

# Изменение существующих данных


def get_change(mode_change):
    change = 1
    while change != 2:
        name_file = input('\nВыберите справочник: ') + '.txt'
        if mode_change == 3:
            with open(name_file, 'r') as file:
                for text in file:
                    print(text)
                file.readlines()
            text_existing = input('Заменяемый текст: ')
            text_replaced = input('Новое значение: ')
            print()
            with fileinput.input(files=name_file, inplace=True, backup=False, mode='r', openhook=None) as file:
                for text in file:
                    print(text.replace(text_existing, text_replaced), end='')
        change = int(
            input('\n 1 - Продолжить изменения:\n 2 - Завершить:\n Input: '))
        print()
    view.get_mode_change()

# Поиск существующих данных


def get_search(mode_change):
    change = 1
    while change != 2:
        name_file = input('\nВыберите справочник: ') + '.txt'
        if mode_change == 4:
            search_text = input('\nВведите поисковой запрос: ')
            with open(name_file, mode='r') as file:
                string = file.readlines()
            for text in string:
                if search_text in text:
                    print(text)
        change = int(
            input('\n 1 - Продолжить изменения:\n 2 - Завершить:\n Input: '))
    view.get_mode_change()

# Выход из программы


def exit(mode):
    if mode == 0:
        sys.exit()
