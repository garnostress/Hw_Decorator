import requests
import json
from _datetime import datetime
from Decorator_2 import get_path, input_path

WIKI_URL = 'https://ru.wikipedia.org/wiki/'
@get_path(input_path)
class Wiki_parser:

    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start -1

    def __iter__(self):
        return self

    def __next__(self):
        country_url = {}
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common'].replace(' ', '_')
        country_link = f'{WIKI_URL}{country}'
        country_url[country] = country_link

        return country_url

if __name__ == '__main__':
    data = Wiki_parser('countries.json', 0)
    with open('country_link.json', 'w', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False, indent=2)
    print('Ссылки по стране успешно сохранены в файл "country_link.json"')