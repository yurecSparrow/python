import os
import shutil

cur_dir = r'D:\учеба\python\venv\my_project'
templ_dir=os.path.join(cur_dir,'templates')
incl_dirs = [*os.walk(cur_dir)]
if not os.path.exists(templ_dir):
    os.mkdir(templ_dir)
incl_dir = [item[0] for item in incl_dirs]
for directory in incl_dir:
    abs_dir = directory.split('\\')
    if abs_dir[len(abs_dir)-2]=='templates':
        src_dir = '\\'.join(abs_dir)
        dst_dir = os.path.join(templ_dir,abs_dir[len(abs_dir)-1])
        shutil.copytree(src_dir,dst_dir)
