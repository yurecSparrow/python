import re

def parse_email(mail):
    RE_EMAIL = re.compile(r'(:?^\S+)@(:?\S+\.\S+$)')
    assert RE_EMAIL.match(mail), f'wrong email'
    mail_parsed = RE_EMAIL.findall(txt)[0]
    user_name = mail_parsed[0]
    domen = mail_parsed[1]
    print(f'user name:{user_name}\ndomen:{domen}')

txt = 'cpt.yurecsparrow@gmail.com'
parse_email(txt)
