from pathlib import Path

# Поиск файлов в директории


def directory(list_data_base):
    directory = '.'
    list = Path(directory).glob('*.txt')
    for file in list:
        list_data_base.append(file)
        print(file)
    return list_data_base


list_data_base = list()
directory(list_data_base)


