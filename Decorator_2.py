from _datetime import datetime
import json

def get_path(path):
    path = f'{path}\log.json'
    def decorator(function):
        def get_info(*args, **kwargs):
            date = datetime.today().replace(microsecond=0)
            new_function = function(*args, **kwargs)
            info = f'Дата и время: {date}, функция: {get_path.__name__}, аргументы: {args}, {kwargs}'
            with open('log_path.json', 'w', encoding='utf-8') as f:
                json.dump(info, f, ensure_ascii=False, indent=2)
            print('Данные загружены в файл', 'log_path.json')
            return new_function
        return get_info

    print(f'Путь к файлу log_path.json:', path)
    return decorator




input_path = input('Введите путь к логам:\n')

@get_path(input_path)
def logger(first_name, last_name):
    return first_name, last_name


logger('Иван', 'Иванов')