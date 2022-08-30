import os
from datetime import datetime, timedelta

dir = 'H:\\Project\\YouTube Twitter URL data'
test_dir = 'D:\\Python\\rebuild-db-for-twitter-url\\test\\'


def clear_file(dir):
    # 获取目录下的文件和文件夹
    dirs = os.listdir(dir)
    # 遍历目录下的文件
    for d in dirs:
        # 拼接到当前目录
        f = os.path.join(dir, d)
        # 判断是否是文件
        if os.path.isfile(f):
            if f.endswith('redirect_info.txt'):
                os.remove(f)
                print('删除: ', f)
            else:
                continue
        else:
            clear_file(f)


clear_file(dir)
