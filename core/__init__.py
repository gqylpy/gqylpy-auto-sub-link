import sys
import uuid
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

from tools import db
from tools import gen_path
from tools import exec_sql
from tools import fetch_pid

from config import DB_DIR
from config import POOL_SIZE

_thread_pool = ThreadPoolExecutor(POOL_SIZE)

_ua = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'

if sys.platform == 'win32':
    _chromedriver = gen_path(DB_DIR, 'chromedriver_windows')
elif sys.platform == 'darwin':
    _chromedriver = gen_path(DB_DIR, 'chromedriver_mac')
else:
    raise BaseException('Unknown system')


def fetch_blog_path() -> tuple:
    """获取新加入的文章链接"""
    return exec_sql(f'''
        SELECT user.blog_path, blog.id
        FROM user INNER JOIN blog
        ON user.id = blog.user_id
        WHERE blog.is_private IS FALSE 
          AND blog.is_draft IS FALSE 
          AND blog.is_delete IS FALSE 
          AND blog.access_password IS NULL
        ORDER BY blog.id DESC
    ''', database=db.hello_world)


def open_chrome(chromedriver_file: str) -> Chrome:
    chrome_options = Options()

    # 隐藏浏览器
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Set UA
    chrome_options.add_argument(f'user-agent="{_ua + str(uuid.uuid4())}"')

    return Chrome(chromedriver_file, chrome_options=chrome_options)


def async_task(data: tuple, chromedriver_file: str):
    bro: Chrome

    try:
        bro = open_chrome(chromedriver_file)
        bro.set_page_load_timeout(10)

        for blog_path, bid in data:
            try:
                bro.get(f'http://blog.gqylpy.com/{blog_path}/{bid}/')
                # bro.execute_script(f'window.open("{link}");')
            except Exception:
                continue

    finally:
        bro.quit()


def main():
    fetch_pid()
    while True:
        async_task(
            data=fetch_blog_path(),
            chromedriver_file=_chromedriver
        )
