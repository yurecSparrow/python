multipls = {dig:0 for dig in range(2,10)}
for dig in multipls.keys():
    for i in range(2,100):
        if i % dig == 0:
            multipls[dig]+=1
for dig in multipls.keys():
    print(f'На {dig} делиться {multipls[dig]} чисел')
