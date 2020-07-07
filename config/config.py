import os


def _gen_path(*args: str) -> 'An absolute path':
    # Generate an absolute path.
    return os.path.abspath(os.path.join(*args))


BASE_DIR = _gen_path(os.path.dirname(os.path.dirname(__file__)))

DB_DIR = _gen_path(BASE_DIR, 'db')
LOG_DIR = _gen_path(BASE_DIR, 'log')

# 文件编码
FE = 'UTF-8'

# 线程/进程池大小
POOL_SIZE = 1
