from _datetime import datetime
import json


def decorator(function):
    def get_info(*args, **kwargs):
        date = datetime.today().replace(microsecond=0)
        new_function = function(*args, **kwargs)
        info = f'Дата и время: {date}, функция: {decorator.__name__}, аргументы: {args}, {kwargs}'
        with open('log.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        print('Данные загружены в файл', 'log.json')
        return new_function
    return get_info


@decorator
def logger(first_name, last_name):
    return first_name, last_name


logger('Иван', 'Иванов')