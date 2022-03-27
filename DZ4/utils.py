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