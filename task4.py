import os

dir_to_analyze=r'D:\учеба\python\venv'
try:
    incl_dirs = [*os.walk(dir_to_analyze)]
    sizes = {}
    for dir in incl_dirs:
        files = dir[len(dir)-1]
        cur_dir = dir[0]
        for file in files:
            full_dir = os.path.join(cur_dir, file)
            size_of_file = os.stat(full_dir).st_size
            key_size=10
            while size_of_file > key_size:
                key_size = key_size * 10
            if key_size not in sizes:
                sizes[key_size] = 1
            else:
                sizes[key_size] = sizes[key_size] +1
    for idx in range(10):
        if 10 ** idx in sizes:
            print(f'{10 ** idx}:{sizes[10 ** idx]}')
except:
    print('Some gone wrong')
