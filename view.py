# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import controller


def get_start():
    print('Добро пожаловать в local-справочник\n')
    mode = int(input('Выберите режим работы программы:\n 1 - Создать новый справочник\n 2 - Изменить существующий справочник\n 0 - Выход из программы\n Input: '))
    controller.exit(mode)
    controller.get_op(mode)


def get_two_start():
    mode = int(input(
        'Выберите режим работы программы:\n 1 - Создать новый справочник\n 0 - Выход из программы\n Input: '))
    controller.exit(mode)
    controller.get_op(mode)


def get_mode_change():
    mode_change = int(input(
        ' 1 - Экспортировать данные\n 2 - Импортировать данные\n 3 - Изменить данные\n 4 - Поиск данных\n 0 - Выход из программы\n Input: '))
    controller.exit(mode_change)
    if mode_change == 1:
        controller.get_read(mode_change)
    elif mode_change == 2:
        controller.get_input(mode_change)
    elif mode_change == 3:
        controller.get_change(mode_change)
    elif mode_change == 4:
        controller.get_search(mode_change)
