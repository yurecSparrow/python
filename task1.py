import os


def cr_folder(fldr):
    if not os.path.exists(fldr):
        os.mkdir(fldr)
    else:
        print(f'Folder {fldr} is also exist')


cur_dir = r'D:\учеба\python\venv'
folder = os.path.join(cur_dir,'my_project')
cr_folder(folder)
cur_dir = folder
cr_folder(os.path.join(cur_dir,'settings'))
cr_folder(os.path.join(cur_dir,'mainapp'))
cr_folder(os.path.join(cur_dir,'adminapp'))
cr_folder(os.path.join(cur_dir,'authapp'))
