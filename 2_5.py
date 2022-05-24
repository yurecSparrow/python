ch_code = 32
while ch_code <= 127:
    s=''
    for i in range(10):
        s += str(ch_code+i) + ' ' + (chr(ch_code+i)+'\t')
        if ch_code+i == 127:
            break
    s += '\n'
    ch_code+=10
    print(s)
