import os
import sys


def fetch_pid(filename: str = 'pid'):
    if sys.platform == 'linux':
        f = open(filename, 'w', encoding='UTF-8')
        f.write(str(os.getpid()))
        f.close()
