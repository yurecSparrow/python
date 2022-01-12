def type_logger(func):
    def print_type(*args):
        for t in args:
            print(type(t), end=', ')
    return print_type

@type_logger
def calc_cube(num, steps):
    return num ** steps

print(calc_cube(5, 'hi'))
