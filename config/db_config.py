class DBS:
    # Database alias
    gqylpy = 'gqylpy'
    hello_world = 'hello_world'

    class Config:
        # Database Config
        gqylpy = dict(
            host='',
            port='',
            user='',
            password='',
            db='',
            charset='utf8',
            autocommit=True,
            connect_timeout=60 * 60 * 24 * 15  # 15 Day
        )
        hello_world = dict(
            host='',
            port='',
            user='',
            password='',
            db='',
            charset='utf8',
            autocommit=True,
            connect_timeout=60 * 60 * 24 * 15
        )
