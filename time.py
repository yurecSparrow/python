duration = int(input("duration:"))
days = duration // 86400
duration %= 86400
hours = duration // 3600
duration %= 3600
minutes = duration // 60
sek = duration % 60
if days:
    print(days, ' дн,', end=' ')
if hours:
    print(hours, ' ч,', end=' ')
if minutes:
    print(minutes, ' м,', end=' ')
if sek:
    print(sek, ' сек,', end=' ')
