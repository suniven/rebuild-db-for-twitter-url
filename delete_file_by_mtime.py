# 根据文件修改时间删除错误的redirect info

import os
from tqdm import tqdm
from datetime import datetime, timedelta

diff = timedelta(days=7)  # 设置需要清理的时间
dir = 'D:\\Project\\Twitter URL data\\'
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
                # print(f)
                # os.path.getmtime获取文件的修改时间戳，在转换成日期
                s = datetime.fromtimestamp(os.path.getmtime(f))
                # print(s.strftime('%Y-%m-%d %H:%M:%S'))
                # 判断文件是否是满足删除条件
                if (datetime.now() - s) > diff:
                    os.remove(f)
                    print('删除: {0} {1}'.format(f, s.strftime('%Y-%m-%d %H:%M:%S')))
            else:
                continue
        # 若不是文件，那就是文件夹（目录），使用递归，继续以上操作
        else:
            clear_file(f)


clear_file(dir)
