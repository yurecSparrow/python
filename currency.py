import sys
import utils


if __name__ == '__main__':
    if len(sys.argv) > 1:
        program, valut_code = sys.argv
    else:
        valut_code = input("Обозначение валюты:")
    utils.get_currency(valut_code)
