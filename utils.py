from requests import get, utils
from datetime import datetime


def get_currency(valut_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    idx_date = content.find("ValCurs Date") + 14
    cur_date = content[idx_date:idx_date + 10]
    date_parts = cur_date.split(".")
    date_response = datetime(year=int(date_parts[2]), month=int(date_parts[1]), day=int(date_parts[0]))
    idx_start = content.find(valut_code.upper())
    content = content[idx_start:]
    idx_value = content.find("<Value>") + 7
    currency = content[idx_value:idx_value + 7]
    currency_float = float(currency[:2]) + float(currency[3:]) / 10000
    print(f'{currency_float}, {date_response.date()}')
    return 0


if __name__ == '__main__':
    char_cd = input("Обозначение валюты:")
    get_currency(char_cd)
