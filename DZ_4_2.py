# Написать функцию currency_rates(),
# принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# # Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import requests
from decimal import *
from datetime import datetime

getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in r:
        return None

    rub = r[r.find('<Value>', r.find(val)) + 7: r.find('</Value>', r.find(val))]
    to_day = r[r.find('Date="') + 6: r.find('"', r.find('Date="') + 6)].split('.')
    day, month, year = map(int,to_day)
    return f'{Decimal(rub.replace(",", "."))}, {datetime(day = day, month = month, year = year)}'

print(currency_rates('USD'))