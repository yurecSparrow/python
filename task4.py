def value_checker(func):
   def check_value(val):
       if (type(val) == int) and (val > 0):
           to_return = func(val)
           return to_return
       else:
           raise ValueError('wrong value')
   return check_value

@value_checker
def cube_num(num):
    return num ** 3

a = 3
b = cube_num(a)
print(b)
