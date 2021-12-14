workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for worker in workers:
    worker_parts = worker.split(' ')
    worker_name = worker_parts.pop()
    print(f'Привет, {worker_name.title()}')
