import os
import random
import shutil
import datetime
import time

backupPath = ''
path = r'C:/Users/Dell/AppData/Local/GeometryDash'
date = str(datetime.datetime.now().date())
pth = r'C:/Users/Dell/Documents/gdbacks'
f_lst = []


def backup(files: list):
    if os.path.exists(fr'C:/Users/Dell/Documents/gdbacks/{date}'):
        n_dir = fr'C:/Users/Dell/Documents/gdbacks/{date}-{len(os.listdir(pth)) + 1}'
        os.mkdir(n_dir)
        for file in files:
            print(file[43:])
            shutil.copyfile(file,
                            fr'{n_dir}/{file[43:]}')
    else:
        nw_dir = fr'C:/Users/Dell/Documents/gdbacks/{date}'
        os.mkdir(nw_dir)
        for file in files:
            print(file)
            shutil.copyfile(file,
                            fr'{nw_dir}/{file[43:]}')


if __name__ == "__main__":
    for f in os.listdir(path):
        if f.endswith('.dat'):
            f_lst.append(path + '/' + f)

    backup(f_lst)
